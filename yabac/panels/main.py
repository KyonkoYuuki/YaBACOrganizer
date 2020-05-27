from functools import partial
import pickle

import wx
import time
from pubsub import pub

from pyxenoverse.bac.entry import Entry
from pyxenoverse.bac.sub_entry import SubEntry, ITEM_TYPES
from pyxenoverse.gui import get_first_item, get_next_item
from pyxenoverse.gui.ctrl.multiple_selection_box import MultipleSelectionBox
from pyxenoverse.gui.ctrl.single_selection_box import SingleSelectionBox
from pyxenoverse.gui.ctrl.unknown_hex_ctrl import UnknownHexCtrl
from pyxenoverse.gui.file_drop_target import FileDropTarget

from yabac.dlg.paste import PasteDialog
from yabac.dlg.convert import ConvertDialog


class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        self.focus = None
        self.bac = None
        self.cdo = None

        self.entry_list = wx.TreeCtrl(self, style=wx.TR_MULTIPLE | wx.TR_HAS_BUTTONS | wx.TR_FULL_ROW_HIGHLIGHT | wx.TR_LINES_AT_ROOT | wx.TR_HIDE_ROOT)
        self.entry_list.SetDropTarget(FileDropTarget(self, "load_bac"))
        self.entry_list.Bind(wx.EVT_TREE_ITEM_MENU, self.on_right_click)
        self.entry_list.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_select)
        self.cdo = wx.CustomDataObject("BACEntry")

        self.append_id = wx.NewId()
        self.insert_id = wx.NewId()
        self.add_copy_id = wx.NewId()
        self.insert_copy_id = wx.NewId()
        self.Bind(wx.EVT_MENU, self.on_open, id=wx.ID_OPEN)
        self.Bind(wx.EVT_MENU, self.on_save, id=wx.ID_SAVE)
        self.Bind(wx.EVT_MENU, self.on_delete, id=wx.ID_DELETE)
        self.Bind(wx.EVT_MENU, self.on_copy, id=wx.ID_COPY)
        self.Bind(wx.EVT_MENU, self.on_paste, id=wx.ID_PASTE)
        self.Bind(wx.EVT_MENU, self.on_add_copy, id=wx.ID_ADD)
        self.Bind(wx.EVT_MENU, self.on_append_bac_entry, id=self.append_id)
        self.Bind(wx.EVT_MENU, self.on_insert_bac_entry, id=self.insert_id)
        self.Bind(wx.EVT_MENU, partial(self.on_add_copy, append=True), id=self.add_copy_id)
        self.Bind(wx.EVT_MENU, partial(self.on_add_copy, append=False), id=self.insert_copy_id)

        accelerator_table = wx.AcceleratorTable([
            (wx.ACCEL_CTRL, ord('c'), wx.ID_COPY),
            (wx.ACCEL_CTRL, ord('v'), wx.ID_PASTE),
            (wx.ACCEL_NORMAL, wx.WXK_DELETE, wx.ID_DELETE),
        ])
        self.entry_list.SetAcceleratorTable(accelerator_table)

        # Publishers
        pub.subscribe(self.convert_for_skill_creator, 'convert_for_skill_creator')
        pub.subscribe(self.update_entry, 'update_entry')
        pub.subscribe(self.update_item, 'update_item')
        pub.subscribe(self.on_select, 'on_select')
        pub.subscribe(self.reindex, 'reindex')
        pub.subscribe(self.set_focus, 'set_focus')
        pub.subscribe(self.clear_focus, 'clear_focus')

        # Use some sizers to see layout options
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.entry_list, 1, wx.ALL | wx.EXPAND, 10)

        # Layout sizers
        self.SetSizer(sizer)
        self.SetAutoLayout(1)

    def enable_selected(self, menu_item, single=True, entry=None):
        selected = self.entry_list.GetSelections()
        if not selected:
            menu_item.Enable(False)
        elif single and len(selected) > 1:
            menu_item.Enable(False)
        elif entry:
            data = self.entry_list.GetItemData(selected[0])
            if data.get_readable_name() != entry.get_readable_name():
                menu_item.Enable(False)

    def on_right_click(self, _):
        menu = wx.Menu()
        sub_entry_menu = wx.Menu()
        append = menu.Append(self.append_id, "&Add Entry", "Add BAC Entry")
        self.enable_selected(append)
        insert = menu.Append(self.insert_id, "&Insert Entry", "Insert BAC Entry")
        self.enable_selected(insert)
        menu.AppendSubMenu(sub_entry_menu, "Add &Subentry")
        for bac_value, bac_type in ITEM_TYPES.items():
            sub_entry_item = sub_entry_menu.Append(-1, bac_type.__name__)
            self.enable_selected(sub_entry_item)
            self.Bind(wx.EVT_MENU, partial(self.on_add_item, bac_value=bac_value), sub_entry_item)
        delete = menu.Append(wx.ID_DELETE, "Delete", "&Delete entry(s)")
        self.enable_selected(delete, single=False)
        copy = menu.Append(wx.ID_COPY, "Copy\tCtrl+C", "&Copy entry(s)")
        self.enable_selected(copy)
        menu.AppendSeparator()
        # Paste options
        paste_data = self.get_paste_data(self.entry_list.GetSelections(), False)
        if not paste_data:
            paste = menu.Append(-1, "<no copied item found>")
            paste.Enable(False)
        else:
            name = paste_data.get_readable_name()
            title = menu.Append(-1, "Copied " + name)
            title.Enable(False)
            paste = menu.Append(wx.ID_PASTE, f"&Paste {name}\tCtrl+V")
            self.enable_selected(paste, entry=paste_data)
            if paste_data.get_name() == 'Entry':
                insert = menu.Append(-1, f"Insert {name} Copy")
                self.enable_selected(insert, entry=paste_data)
                self.Bind(wx.EVT_MENU, partial(self.on_add_copy, append=False), insert)
                append = menu.Append(-1, f"Append {name} Copy")
                self.enable_selected(append, entry=paste_data)
                self.Bind(wx.EVT_MENU, partial(self.on_add_copy, append=True), append)
            else:
                add = menu.Append(-1, f"Add {name} Copy")
                self.enable_selected(add, entry=paste_data)
                self.Bind(wx.EVT_MENU, partial(self.on_add_copy, append=True), add)

        self.PopupMenu(menu)
        menu.Destroy()

    def on_open(self, _):
        pub.sendMessage('open_bac', e=None)

    def on_save(self, _):
        pub.sendMessage('save_bac', e=None)

    def convert_for_skill_creator(self):
        if not self.bac:
            with wx.MessageDialog(self, "No BAC loaded!", "Error") as dlg:
                dlg.ShowModal()
            return

        # Get Choices
        choices = set()
        item, _ = get_first_item(self.entry_list)
        while item.IsOk():
            data = self.entry_list.GetItemData(item)
            item = get_next_item(self.entry_list, item)
            if 'skill_id' not in data.__fields__:
                continue
            if data.skill_id != 0 and data.skill_id != 0xFFFF and data.skill_id != 0xBACA:
                choices.update([str(data.skill_id)])

        if not choices:
            with wx.MessageDialog(self, "Cannot find any Skill IDs to convert", "Error") as dlg:
                dlg.ShowModal()
            return

        # Show Dialog
        with ConvertDialog(self, list(choices)) as dlg:
            if dlg.ShowModal() != wx.ID_OK:
                return
            skill_id = dlg.GetValue()

        # Do conversion
        item, _ = get_first_item(self.entry_list)
        changed = 0
        while item.IsOk():
            data = self.entry_list.GetItemData(item)
            if 'skill_id' in data.__fields__ and data.skill_id == skill_id:
                data.skill_id = 0xBACA
                changed += 1
            item = get_next_item(self.entry_list, item)
        self.on_select(None)
        pub.sendMessage('set_status_bar', text=f'Changed {changed} skill ids to 0xBACA')

    def expand_parents(self, item):
        root = self.entry_list.GetRootItem()
        parent = self.entry_list.GetItemParent(item)
        while parent != root:
            self.entry_list.Expand(parent)
            parent = self.entry_list.GetItemParent(parent)

    def select_item(self, item):
        self.entry_list.UnselectAll()
        self.entry_list.SelectItem(item)
        self.expand_parents(item)
        if not self.entry_list.IsVisible(item):
            self.entry_list.ScrollTo(item)
        self.on_select(None)

    def get_selected_root_nodes(self):
        selected = self.entry_list.GetSelections()
        if not selected:
            return []
        root = self.entry_list.GetRootItem()

        nodes = []
        for item in selected:
            parent = self.entry_list.GetItemParent(item)
            while parent != root and parent.IsOk():
                if parent in selected:
                    break
                parent = self.entry_list.GetItemParent(parent)
            if parent == root:
                nodes.append(item)
        return nodes

    def on_select(self, _):
        if not self.entry_list:
            return
        selected = self.entry_list.GetSelections()
        if len(selected) != 1:
            pub.sendMessage('hide_panels')
            return
        entry = self.entry_list.GetItemData(selected[0])
        pub.sendMessage('load_entry', item=selected[0], entry=entry)

    def update_entry(self, item, entry):
        self.entry_list.SetItemText(item, f'{entry.index}: Entry (0x{entry.flags:X})')

    def update_item(self, item, entry):
        parent = self.entry_list.GetItemParent(item)
        self.entry_list.Delete(item)
        child = self.entry_list.GetFirstChild(parent)[0]
        index = 0
        while child.IsOk():
            if self.entry_list.GetItemData(child).start_time > entry.start_time:
                new_item = self.entry_list.InsertItem(
                    parent, index, str(entry.start_time), data=entry)
                break
            child = self.entry_list.GetNextSibling(child)
            index += 1
        else:
            new_item = self.entry_list.AppendItem(
                parent, f'{entry.index}: {entry.start_time}', data=entry)
        self.select_item(new_item)
        return new_item

    def build_tree(self):
        self.entry_list.DeleteAllItems()
        self.entry_list.Refresh()
        hidden = self.parent.hidden.GetValue()
        self.entry_list.AddRoot("Entries")
        for i, entry in enumerate(self.bac.entries):
            if not entry.sub_entries and hidden:
                continue
            entry_item = self.entry_list.AppendItem(
                self.entry_list.GetRootItem(), f'{entry.index}: Entry (0x{entry.flags:X})', data=entry)
            self.build_entry_tree(entry_item, entry)

    def build_entry_tree(self, entry_item, entry):
        hidden = self.parent.hidden.GetValue()
        for sub_entry in entry.sub_entries:
            if not sub_entry.items and hidden:
                continue
            sub_entry_item = self.entry_list.AppendItem(
                entry_item, f'{sub_entry.type}: {sub_entry.get_type_name()}', data=sub_entry)
            self.build_sub_entry_tree(sub_entry_item, sub_entry)

    def build_sub_entry_tree(self, sub_entry_item, sub_entry):
        for item in sub_entry.items:
            self.entry_list.AppendItem(sub_entry_item, str(item.start_time), data=item)

    def reindex(self, selected=None):
        for i, entry in enumerate(self.bac.entries):
            entry.index = i
            # entry.flags = entry.flags & 0xF if len(entry.sub_entries) > 0 else (entry.flags & 0x0F) | 0x80000000
            entry.sub_entries.sort(key=lambda n: n.type)
            for j, sub_entry in enumerate(entry.sub_entries):
                sub_entry.index = j
                sub_entry.items.sort(key=lambda n: n.start_time)
                for k, item in enumerate(sub_entry.items):
                    item.index = k

        item, _ = get_first_item(self.entry_list)
        hidden = self.parent.hidden.GetValue()

        # Fix tree names
        while item.IsOk():
            to_delete = None
            data = self.entry_list.GetItemData(item)
            if data.get_name() == 'Entry':
                if selected != item and hidden and not self.entry_list.GetFirstChild(item)[0].IsOk():
                    to_delete = item
                else:
                    self.entry_list.SetItemText(item, f'{data.index}: Entry (0x{data.flags:X})')
            elif data.get_name() == 'SubEntry':
                if selected != item and hidden and not self.entry_list.GetFirstChild(item)[0].IsOk():
                    to_delete = item
                else:
                    self.entry_list.SetItemText(item, f'{data.type}: {data.get_type_name()}')
                    sub_entry = self.entry_list.GetItemData(item)
                    for entry in sub_entry.items:
                        item = get_next_item(self.entry_list, item)
                        self.entry_list.SetItemData(item, entry)
                        self.entry_list.SetItemText(item, str(entry.start_time))
            item = get_next_item(self.entry_list, item)
            if to_delete:
                self.entry_list.Delete(to_delete)

    def get_entry_item_pair(self, entry):
        return entry, self.entry_list.GetItemData(entry)

    def get_parent_bac_entry(self, bac_entry):
        if bac_entry:
            return self.get_entry_item_pair(bac_entry)
        bac_entry = self.entry_list.GetSelections()[0]
        while bac_entry.IsOk():
            data = self.entry_list.GetItemData(bac_entry)
            if data.get_name() == 'Entry':
                return self.get_entry_item_pair(bac_entry)
            bac_entry = self.entry_list.GetItemParent(bac_entry)
        else:
            return None, None

    def add_bac_entry(self, append, bac_entry=None):
        bac_entry, data = self.get_parent_bac_entry(bac_entry)
        if not bac_entry or not data:
            return

        # Check if append or insert
        new_index = data.index
        if append:
            new_index += 1

        # Add Entry
        new_entry = Entry(self.bac, new_index)
        self.bac.entries.insert(new_index, new_entry)

        # Insert into Treelist
        root = self.entry_list.GetRootItem()
        new_item = self.entry_list.InsertItem(root, new_index, f'{new_index}: Entry', data=new_entry)
        return new_item, new_entry

    def add_sub_entry(self, bac_value, bac_entry=None):
        bac_entry, data = self.get_parent_bac_entry(bac_entry)
        if not bac_entry or not data:
            return None, None

        # Try to find the sub_entry first
        item = self.entry_list.GetFirstChild(bac_entry)[0]
        while item.IsOk():
            sub_entry = self.entry_list.GetItemData(item)
            if sub_entry.type == bac_value:
                return item, sub_entry
            item = self.entry_list.GetNextSibling(item)

        # If not found, create a new one
        new_sub_entry = SubEntry(0)
        new_sub_entry.type = bac_value
        data.sub_entries.append(new_sub_entry)
        data.sub_entries.sort(key=lambda n: n.type)

        # Reindex real fast
        for i, sub_entry in enumerate(data.sub_entries):
            sub_entry.index = i

        # Try to insert it into the tree at the right place
        index = 0
        item = self.entry_list.GetFirstChild(bac_entry)[0]
        for i in range(new_sub_entry.index):
            if not item.IsOk():
                break
            item = self.entry_list.GetNextSibling(item)
            index += 1
        new_item = self.entry_list.InsertItem(
            bac_entry, index, f'{new_sub_entry.type}: {new_sub_entry.get_type_name()}', data=new_sub_entry)
        return new_item, new_sub_entry

    def add_item(self, bac_value, copied_entry=None, bac_entry=None):
        if copied_entry and bac_value != copied_entry.type:
            with wx.MessageDialog(self, f"Data format doesn't match '{ITEM_TYPES[bac_value].__name__}' type") as dlg:
                dlg.ShowModal()
            return

        # Get BAC entry
        bac_entry, data = self.get_parent_bac_entry(bac_entry)
        if not bac_entry or not data:
            return

        # Get or add sub_entry
        sub_entry, sub_entry_data = self.add_sub_entry(bac_value, bac_entry)

        # Create new item
        new_bac_type = ITEM_TYPES[bac_value](0)
        new_bac_type.paste(copied_entry)

        # Add it to sub_entry
        sub_entry_data.items.append(new_bac_type)
        sub_entry_data.items.sort(key=lambda n: n.start_time)

        # Add to correct place in tree list
        index = 0
        item = self.entry_list.GetFirstChild(sub_entry)[0]
        while item.IsOk():
            if new_bac_type.start_time <= self.entry_list.GetItemData(item).start_time:
                break
            item = self.entry_list.GetNextSibling(item)
            index += 1
        new_item = self.entry_list.InsertItem(sub_entry, index, '', data=new_bac_type)
        return new_item, new_bac_type

    def on_insert_bac_entry(self, _):
        new_item, _ = self.add_bac_entry(False)
        self.select_item(new_item)
        self.reindex(new_item)
        pub.sendMessage('set_status_bar', text="Inserted new Entry")

    def on_append_bac_entry(self, _):
        new_item, _ = self.add_bac_entry(True)
        self.select_item(new_item)
        self.reindex(new_item)
        pub.sendMessage('set_status_bar', text="Added new Entry")

    def on_add_item(self, _, bac_value):
        new_item, _ = self.add_item(bac_value)
        self.select_item(new_item)
        self.reindex(new_item)
        self.on_select(None)
        pub.sendMessage('set_status_bar', text=f"Added new {ITEM_TYPES[bac_value].__name__}")

    def on_delete(self, _):
        # Get only the parents and select them.
        selected = self.get_selected_root_nodes()
        data = [self.entry_list.GetItemData(item) for item in selected]
        if not selected:
            return
        # First unselect children if parents are chosen
        delete_bac = True

        # See if bac entries are part of the selected
        if any(isinstance(entry, Entry) for entry in data):
            with wx.MessageDialog(self, 'Delete BAC entry(s) as well?', style=wx.YES | wx.NO | wx.CANCEL) as dlg:
                res = dlg.ShowModal()
                if res == wx.ID_YES:
                    delete_bac = True
                elif res == wx.ID_NO:
                    delete_bac = False
                else:
                    return

        # Loop over and delete
        for item in reversed(selected):
            data = self.entry_list.GetItemData(item)
            if data.get_name() == 'Entry':
                if delete_bac:
                    self.bac.entries.remove(data)
                    self.entry_list.Delete(item)
                else:
                    self.bac.entries[data.index].sub_entries.clear()
                    child = self.entry_list.GetFirstChild(item)[0]
                    while child.IsOk():
                        sibling, child = child, self.entry_list.GetNextSibling(child)
                        self.entry_list.Delete(sibling)
            elif data.get_name() == 'SubEntry':
                parent = self.entry_list.GetItemData(self.entry_list.GetItemParent(item))
                parent.sub_entries.remove(data)
                self.entry_list.Delete(item)
            else:
                parent = self.entry_list.GetItemData(self.entry_list.GetItemParent(item))
                parent.items.remove(data)
                self.entry_list.Delete(item)
        self.reindex()
        pub.sendMessage('set_status_bar', text="Deleted successfully")

    def on_copy(self, _):
        selected = self.entry_list.GetSelections()
        if len(selected) > 1:
            with wx.MessageDialog(self, 'Can only copy one entry at a time') as dlg:
                dlg.ShowModal()
            return
        entry = self.entry_list.GetItemData(selected[0])
        self.cdo = wx.CustomDataObject('BAC')
        self.cdo.SetData(pickle.dumps(entry))
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(self.cdo)
            wx.TheClipboard.Flush()
            wx.TheClipboard.Close()
        pub.sendMessage('set_status_bar', text=f'Copied {entry.get_readable_name()}')

    def get_paste_data(self, selected, warn=True):
        if len(selected) > 1 and warn:
            with wx.MessageDialog(self, 'Can only paste one entry at a time') as dlg:
                dlg.ShowModal()
            return None
        cdo = wx.CustomDataObject('BAC')
        success = False
        if wx.TheClipboard.Open():
            success = wx.TheClipboard.GetData(cdo)
            wx.TheClipboard.Close()
        if success:
            return pickle.loads(cdo.GetData())
        return None

    def on_paste(self, _):
        selected = self.entry_list.GetSelections()
        paste_data = self.get_paste_data(selected)
        if not paste_data:
            return
        item = selected[0]
        expanded = self.entry_list.IsExpanded(item)
        entry = self.entry_list.GetItemData(item)

        if type(paste_data) != type(entry):
            with wx.MessageDialog(self, f"Unable to paste '{paste_data.get_readable_name()}' type "
                                  f"onto '{entry.get_readable_name()}'") as dlg:
                dlg.ShowModal()
            return

        entry_values = entry.get_static_values()
        paste_values = paste_data.get_static_values()

        # Display dialog for stuff that might have changed
        changed_values = {}
        if paste_values:
            with PasteDialog(self, entry, paste_values, entry_values) as dlg:
                ret = dlg.ShowModal()
                if ret == wx.ID_YES:
                    changed_values = dlg.GetValue()
                elif ret == wx.ID_CANCEL:
                    return

        # Paste Data
        entry.paste(paste_data, changed_values)

        # Delete Children
        child = self.entry_list.GetFirstChild(item)[0]
        while child.IsOk():
            current, child = child, self.entry_list.GetNextSibling(child)
            self.entry_list.Delete(current)
        if not item or not entry:
            return

        # Rebuild Tree
        class_name = entry.get_name()
        if class_name == 'Entry':
            self.build_entry_tree(item, entry)
        elif class_name == 'SubEntry':
            self.build_sub_entry_tree(item, entry)
        else:
            self.update_item(item, entry)

        # Expand item if it was already expanded
        if expanded:
            self.entry_list.Expand(item)
        self.reindex()
        pub.sendMessage('set_status_bar', text=f"Pasted {paste_data.get_readable_name()}")

    def on_add_copy(self, _, append=True):
        selected = self.entry_list.GetSelections()
        paste_data = self.get_paste_data(selected)
        if not paste_data:
            return
        class_name = paste_data.get_name()
        if class_name == 'Entry':
            new_entry, new_entry_data = self.add_bac_entry(append, selected[0])
            new_entry_data.paste(paste_data, copy_sub_entries=False)
            self.select_item(new_entry)
            for sub_entry in paste_data.sub_entries:
                for item in sub_entry.items:
                    new_item, new_item_data = self.add_item(item.type, item)
                    new_item_data.paste(item)
            self.entry_list.Expand(new_entry)
        elif class_name == 'SubEntry':
            for item in paste_data.items:
                new_item, new_item_data = self.add_item(item.type, item)
                new_item_data.paste(item)
        else:
            new_item, new_item_data = self.add_item(paste_data.type, paste_data)
            new_item_data.paste(paste_data)
        self.reindex()
        pub.sendMessage('set_status_bar', text=f"Added {paste_data.get_readable_name()}")

    def set_focus(self, focus):
        if type(focus.GetParent()) in (wx.SpinCtrlDouble, UnknownHexCtrl, SingleSelectionBox, MultipleSelectionBox):
            self.focus = focus.GetParent()
        elif type(focus.GetParent().GetParent()) in (SingleSelectionBox, MultipleSelectionBox):
            self.focus = focus.GetParent().GetParent()
        else:
            self.focus = focus

    def clear_focus(self):
        self.focus = None
