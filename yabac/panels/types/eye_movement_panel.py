from yabac.panels.types import BasePanel


class EyeMovementPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.u_08 = self.add_hex_entry(self.unknown_page, 'U_08')

        self.direction_type = self.add_single_selection_entry(self.entry_page, 'Next Direction (Move to)', majorDimension=5, choices={
            'Left (0x0)': 0x0,
            'Up (0x1)': 0x1,
            'Right (0x2)': 0x2,
            'Left (0x3)': 0x3,
            'None (0x4)': 0x4,
            'Right (0x5)': 0x5,
            'Left-Down (0x6)': 0x6,
            'Down (0x7)': 0x7,
            'Right-Down (0x8)': 0x8,
        })
        self.u_0c = self.add_single_selection_entry(self.entry_page, 'Previous Eye Direction (Move From)', majorDimension=5, choices={
            'Left (0x0)': 0x0,
            'Up (0x1)': 0x1,
            'Right (0x2)': 0x2,
            'Left (0x3)': 0x3,
            'None (0x4)': 0x4,
            'Right (0x5)': 0x5,
            'Left-Down (0x6)': 0x6,
            'Down (0x7)': 0x7,
            'Right-Down (0x8)': 0x8,
        })

        self.f_18 = self.add_float_entry(self.entry_page, 'Left Eye Rotation %')
        self.f_1c = self.add_float_entry(self.entry_page, 'Right Eye Rotation %')

        self.rotation = self.add_num_entry(self.entry_page, 'Frames until eyes reach position')
        self.eye_duration = self.add_num_entry(self.entry_page, 'Eye Movement Duration')
        self.u_16 = self.add_hex_entry(self.unknown_page, 'U_16', max=0xFFFF)

