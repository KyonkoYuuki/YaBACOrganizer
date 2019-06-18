from yabac.panels.types import BasePanel


class TargetingAssistancePanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.rotation_axis = self.add_single_selection_entry(
            self.entry_page, 'Rotation Axis', majorDimension=4, choices={
                'X': 0x0,
                'Y': 0x1,
                'Z': 0x2,
                'Unknown (0x3)': 0x3,
                'Unknown (0x4)': 0x4,
                'Unknown (0x8)': 0x8,
                'Unknown (0xC)': 0xC,
            })
        self.u_0a = self.add_hex_entry(self.unknown_page, 'U_0A', max=0xFFFF)
