import wx



class OffsetDialog(wx.Dialog):
    def __init__(self, parent, Title, *args, **kw):
        super().__init__(parent, *args, **kw)
        self.SetTitle(Title)

        self.offset_ctrl = wx.SpinCtrl(self, -1, '', size=(150, -1), style=wx.TE_PROCESS_ENTER)
        # self.find_ctrl.Bind(wx.EVT_TEXT_ENTER, self.on_find)
        self.offset_ctrl.SetFocus()


        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(wx.StaticText(self, -1, 'Offset time:'), 0, wx.ALL, 10)

        self.grid_sizer = wx.FlexGridSizer(rows=4, cols=2, hgap=10, vgap=10)
        self.grid_sizer.Add(self.offset_ctrl, 0, wx.EXPAND)
        hsizer.Add(self.grid_sizer, 0, wx.ALL, 10)





        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        ok_button = wx.Button(self, wx.ID_OK, "Ok")
        ok_button.SetDefault()
        button_sizer.Add(ok_button)
        cancel_button = wx.Button(self, wx.ID_CANCEL, "Cancel")
        button_sizer.AddSpacer(10)
        button_sizer.Add(cancel_button)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(hsizer, 0, wx.EXPAND, 10)
        sizer.Add(wx.StaticLine(self, size=(300, -1)), 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(button_sizer, 0, wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, 10)

        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()

    def GetValue(self):
        return int(self.offset_ctrl.GetValue())
