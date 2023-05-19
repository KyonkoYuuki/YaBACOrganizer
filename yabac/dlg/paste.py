from collections import defaultdict
from pyxenoverse.gui import get_first_item, get_next_item

import wx


def unsnake_case(text):
    return text.replace('_', ' ').capitalize()


class PasteDialog(wx.Dialog):
    def __init__(self, parent, entry, pasted_values, curr_values, *args, **kw):
        super().__init__(parent, *args, **kw)
        self.entry_list = parent.entry_list
        self.entry = entry

        self.SetTitle('Replace pasted entry indexes with original index?')
        sizer = wx.BoxSizer(wx.VERTICAL)
        font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.links = {}
        self.conflict_links = []

        for item_type, v1 in pasted_values.items():
            label = wx.StaticText(self, -1, item_type.__name__)
            label.SetFont(font)
            sizer.Add(label, 0, wx.ALL | wx.CENTER, 10)
            self.links[item_type] = {}
            for entry_pair, v2 in v1.items():
                entry = entry_pair[0]
                dependency = entry_pair[1]
                for depend_value, entry_values in v2.items():
                    if dependency:
                        sizer.Add(wx.StaticText(
                            self, -1,
                            f'{unsnake_case(dependency)} '
                            f'({item_type.dependencies[entry_pair][depend_value]}): '), 0,
                            wx.ALL, 5
                        )
                    grid_sizer = wx.FlexGridSizer(rows=len(entry_values), cols=3, hgap=10, vgap=10)
                    sizer.Add(grid_sizer, 0, wx.ALL, 10)
                    choices = ['No Change']
                    if item_type in curr_values and entry_pair in curr_values[item_type] and depend_value in curr_values[item_type][entry_pair]:
                        choices.extend([str(val) if val < 0x8000 else f'0x{val:X}'
                                        for val in sorted(curr_values[item_type][entry_pair][depend_value])])
                    new_entry_choice = self.find_next_available_index(item_type, entry, dependency, depend_value)
                    choices.append(f'{new_entry_choice} (new entry)')
                    for n, value in enumerate(sorted(entry_values)):
                        ctrl = wx.Choice(self, -1, choices=choices)
                        if n + 1 >= len(choices) - 1 or (n + 1 < len(choices) - 1 and int(choices[n + 1], 0) == value):
                            ctrl.Select(0)
                            find_value = value
                        else:
                            ctrl.Select(n + 1)
                            find_value = int(ctrl.GetString(n + 1))

                        found_conflict = self.find(item_type, entry, find_value)
                        if found_conflict:
                            ctrl.Select(len(choices) - 1)
                            find_value = new_entry_choice
                        conflict = wx.StaticText(self, -1, self.find(item_type, entry, find_value))
                        self.links[item_type][entry_pair] = {depend_value: [value, ctrl]}
                        self.conflict_links.append((ctrl, conflict, item_type, entry, value))

                        grid_sizer.Add(wx.StaticText(
                            self, -1, f' - {unsnake_case(entry)}: {value if value < 0x8000 else f"0x{value:X}"} ->'),
                            0, wx.TOP, 5)
                        grid_sizer.Add(ctrl)
                        grid_sizer.Add(conflict)

        replace_button = wx.Button(self, wx.ID_YES, "Replace")
        replace_button.SetDefault()
        keep_button = wx.Button(self, wx.ID_NO, "Keep All")
        cancel_button = wx.Button(self, wx.ID_CANCEL, "Cancel")

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(replace_button, 0, wx.LEFT | wx.RIGHT, 2)
        button_sizer.Add(keep_button, 0, wx.LEFT | wx.RIGHT, 2)
        button_sizer.Add(cancel_button, 0, wx.LEFT | wx.RIGHT, 5)

        sizer.Add(wx.StaticLine(self, size=(400, -1)), 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(button_sizer, 0, wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, 10)

        self.Bind(wx.EVT_CHOICE, self.on_choice)
        self.Bind(wx.EVT_BUTTON, self.on_close)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()

    def find_next_available_index(self, item_type, entry, dependency, depend_value):
        max_value = 0
        item = get_first_item(self.entry_list)[0]
        while item.IsOk():
            data = self.entry_list.GetItemData(item)
            if isinstance(data, item_type) and \
                    (not dependency or data[dependency] == depend_value) and data[entry] != 0xFFFF:
                max_value = max(data[entry], max_value)

            item = get_next_item(self.entry_list, item)
        return max_value + 1

    def find(self, item_type, entry_type, value):
        item = get_first_item(self.entry_list)[0]
        while item.IsOk():
            data = self.entry_list.GetItemData(item)
            if self.entry == data:
                item = self.entry_list.GetNextSibling(item)
                continue
            elif isinstance(data, item_type) and data[entry_type] == value:
                return 'Conflict Found!'
            item = get_next_item(self.entry_list, item)
        return ''

    def on_close(self, e):
        self.EndModal(e.GetId())

    def on_choice(self, _):
        for ctrl, conflict, item_type, entry_type, default in self.conflict_links:
            selection = ctrl.GetSelection()
            if selection == 0:
                find_value = default
            else:
                find_value = int(ctrl.GetString(selection).split(' ')[0])
            conflict.SetLabelText(self.find(item_type, entry_type, find_value))

    def GetValue(self):
        res = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
        for item_type, v1 in self.links.items():
            for entry_pair, v2 in v1.items():
                for depend_value, entry in v2.items():
                    old_value = entry[0]
                    ctrl = entry[1]
                    selection = ctrl.GetSelection()
                    if selection == 0:
                        new_value = None
                    else:
                        new_value = int(ctrl.GetString(ctrl.GetSelection()).split(' ')[0], 0)
                    res[item_type][entry_pair][depend_value][old_value] = new_value
        return res
