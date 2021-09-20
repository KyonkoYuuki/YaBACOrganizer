import wx
from yabac.panels.types import BasePanel


class BoneModificationPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.modification = self.add_multiple_selection_entry(
            self.entry_page, 'Modification', orient=wx.VERTICAL, cols=2, choices=[
                ('', [], True),
                ('', ['Head', 'Spine Up/Down', 'Spine Left/Right'], True),
            ])
        self.u_0a = self.add_hex_entry(self.unknown_page, 'U_0A', max=0xFFFF)
