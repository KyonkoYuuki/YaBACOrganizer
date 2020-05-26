import wx
from pubsub import pub
from wx.lib.scrolledpanel import ScrolledPanel

from pyxenoverse.gui import add_entry, EVT_RESULT, EditThread
from pyxenoverse.gui.ctrl.hex_ctrl import HexCtrl
from pyxenoverse.gui.ctrl.multiple_selection_box import MultipleSelectionBox
from pyxenoverse.gui.ctrl.single_selection_box import SingleSelectionBox
from pyxenoverse.gui.ctrl.text_ctrl import TextCtrl
from pyxenoverse.gui.ctrl.unknown_hex_ctrl import UnknownHexCtrl

MAX_UINT16 = 0xFFFF
MAX_UINT32 = 0xFFFFFFFF
BONE_TYPES = {
    'Base': 0x0,
    'Pelvis': 0x1,
    'Head': 0x2,
    'Unknown (0x3)': 0x3,
    'Unknown (0x4)': 0x4,
    'Unknown (0x5)': 0x5,
    'Unknown (0x6)': 0x6,
    'Right hand': 0x7,
    'Left hand': 0x8,
    'Unknown (0x9)': 0x9,
    'Unknown (0xa)': 0xa,
    'Unknown (0xb)': 0xb,
    'Unknown (0xc)': 0xc,
    'Unknown (0xd)': 0xd,
    'Unknown (0xe)': 0xe,
    'Unknown (0xf)': 0x0f,
    'Unknown (0x10)': 0x10,
    'Unknown (0x11)': 0x11,
    'Unknown (0x12)': 0x12,
    'Left foot': 0x13,
    'Left wrist': 0x14,
    'Right foot': 0x15,
    'Right wrist': 0x16,
    'Unknown (0x17)': 0x17,
    'Unknown (0x18)': 0x18,
}


class Page(ScrolledPanel):
    def __init__(self, parent, rows=32):
        ScrolledPanel.__init__(self, parent)
        self.sizer = wx.FlexGridSizer(rows=rows, cols=2, hgap=10, vgap=10)
        self.SetSizer(self.sizer)
        self.SetupScrolling()


class BasePanel(wx.Panel):
    def __init__(self, parent, root, name, item_type):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        self.root = root
        self.item = None
        self.entry = None
        self.saved_values = {}
        self.item_type = item_type
        self.edit_thread = None

        self.notebook = wx.Notebook(self)
        self.entry_page = Page(self.notebook)
        self.unknown_page = Page(self.notebook)

        self.notebook.AddPage(self.entry_page, name)
        self.notebook.AddPage(self.unknown_page, 'Unknown')

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.notebook, 1, wx.ALL | wx.EXPAND, 10)

        self.start_time = self.add_num_entry(self.entry_page, 'Start Time')
        self.duration = self.add_num_entry(self.entry_page, 'Duration')
        self.u_04 = self.add_hex_entry(self.unknown_page, 'U_04', max=0xFFFF)
        self.character_type = self.add_single_selection_entry(
            self.entry_page, 'Character Type', -1, choices={
                'Both': 0x0,
                'CAC Only': 0x01,
                'Roster Only': 0x02
            })
        # self.Bind(wx.EVT_SET_FOCUS, self.on_focus)
        self.Bind(wx.EVT_TEXT, self.on_edit)
        self.Bind(wx.EVT_CHECKBOX, self.save_entry)
        self.Bind(wx.EVT_RADIOBOX, self.save_entry)
        EVT_RESULT(self, self.save_entry)

        pub.subscribe(self.focus_on, 'focus_on')

        self.SetSizer(sizer)
        self.SetAutoLayout(1)

    def __getitem__(self, item):
        return self.__getattribute__(item)

    @add_entry
    def add_hex_entry(self, panel, _, *args, **kwargs):
        return HexCtrl(panel, *args, **kwargs)

    @add_entry
    def add_text_entry(self, panel, _, *args, **kwargs):
        if 'size' not in kwargs:
            kwargs['size'] = (150, -1)
        return TextCtrl(panel, *args, **kwargs)

    @add_entry
    def add_num_entry(self, panel, _, *args, **kwargs):
        if 'size' not in kwargs:
            kwargs['size'] = (150, -1)
        kwargs['min'], kwargs['max'] = 0, 65535
        return wx.SpinCtrl(panel, *args, **kwargs)

    @add_entry
    def add_single_selection_entry(self, panel, _, *args, **kwargs):
        return SingleSelectionBox(panel, *args, **kwargs)

    @add_entry
    def add_multiple_selection_entry(self, panel, _, *args, **kwargs):
        return MultipleSelectionBox(panel, *args, **kwargs)

    @add_entry
    def add_unknown_hex_entry(self, panel, _, *args, **kwargs):
        if 'size' not in kwargs:
            kwargs['size'] = (150, -1)
        return UnknownHexCtrl(panel, *args, **kwargs)

    @add_entry
    def add_float_entry(self, panel, _, *args, **kwargs):
        if 'size' not in kwargs:
            kwargs['size'] = (150, -1)
        if 'min' not in kwargs:
            kwargs['min'] = -3.402823466e38
        if 'max' not in kwargs:
            kwargs['max'] = 3.402823466e38

        return wx.SpinCtrlDouble(panel, *args, **kwargs)

    def add_nameable_float_entry(self, panel, *args, **kwargs):
        label = wx.StaticText(panel, -1, '')
        panel.sizer.Add(label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        control = self.add_float_entry(panel, None, *args, **kwargs)
        return label, control

    def on_edit(self, _):
        if not self.edit_thread:
            self.edit_thread = EditThread(self)
        else:
            self.edit_thread.new_sig()

    def hide_entry(self, name):
        try:
            label = self.__getattribute__(name + '_label')
            label.SetLabelText('')
        except AttributeError:
            pass
        control = self.__getattribute__(name)
        if control.IsEnabled():
            control.Disable()
            self.saved_values[name] = control.GetValue()
            control.SetValue(0.0)

    def show_entry(self, name, text, default=None):
        try:
            label = self.__getattribute__(name + '_label')
            label.SetLabelText(text)
        except AttributeError:
            pass
        control = self.__getattribute__(name)
        if not control.IsEnabled():
            control.Enable()
            control.SetValue(self.saved_values.get(name, default))

    def load_entry(self, item, entry):
        self.item = item
        self.saved_values = {}
        for name in entry.__fields__:
            self[name].SetValue(entry[name])
        self.entry = entry

    def save_entry(self, _):
        self.edit_thread = None
        if self.entry is None:
            return
        start_time = self.entry.start_time
        for name in self.entry.__fields__:
            control = self[name]
            # SpinCtrlDoubles suck
            if isinstance(control, wx.SpinCtrlDouble):
                try:
                    self.entry[name] = float(control.Children[0].GetValue())
                except ValueError:
                    # Keep old value if its mistyped
                    pass
            else:
                self.entry[name] = control.GetValue()

        if self.entry.start_time != start_time:
            pub.sendMessage('update_item', item=self.item, entry=self.entry)
            pub.sendMessage('reindex')

    def focus_on(self, entry):
        if not self.IsShown():
            return
        page = self.notebook.FindPage(self[entry].GetParent())
        self[entry].SetFocus()
        self.notebook.ChangeSelection(page)

    def on_focus(self, e):
        pub.sendMessage('set_focus', focus=e.GetWindow())

