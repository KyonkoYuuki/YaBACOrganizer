import wx
from pubsub import pub
from pyxenoverse.gui.ctrl.hex_ctrl import HexCtrl
from yabac.panels.types import add_entry, Page


class EntryPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        self.item = None
        self.entry = None

        self.notebook = wx.Notebook(self)
        self.entry_page = Page(self.notebook)
        self.notebook.AddPage(self.entry_page, 'Entry')

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.notebook, 1, wx.ALL | wx.EXPAND, 10)

        self.flags = self.add_hex_entry(self.entry_page, 'Flags')
        self.Bind(wx.EVT_TEXT, self.save_entry)

        self.SetSizer(sizer)
        self.SetAutoLayout(1)

    @add_entry
    def add_hex_entry(self, panel, _, *args, **kwargs):
        return HexCtrl(panel, *args, **kwargs)

    def load_entry(self, item, entry):
        self.item = item
        self.entry = entry
        self.flags.SetValue(entry.flags)

    def save_entry(self, _):
        if self.entry is None:
            return
        self.entry.flags = self.flags.GetValue()
        pub.sendMessage('update_entry', item=self.item, entry=self.entry)
