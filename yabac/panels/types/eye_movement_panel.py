from yabac.panels.types import BasePanel


class EyeMovementPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.u_08 = self.add_hex_entry(self.unknown_page, 'U_08')

        self.next_direction = self.add_single_selection_entry(self.entry_page, 'Next Direction (Move to)', majorDimension=5, choices={
            'Left (0x0)': 0x0,
            'Up (0x1)': 0x1,
            'Right (0x2)': 0x2,
            'Left-Up (0x3)': 0x3,
            'None (0x4)': 0x4,
            'Right-Up (0x5)': 0x5,
            'Left-Down (0x6)': 0x6,
            'Down (0x7)': 0x7,
            'Right-Down (0x8)': 0x8,
        })
        self.previous_eye_direction = self.add_single_selection_entry(self.entry_page, 'Previous Eye Direction (Move From)', majorDimension=5, choices={
            'Left (0x0)': 0x0,
            'Up (0x1)': 0x1,
            'Right (0x2)': 0x2,
            'Left-Up (0x3)': 0x3,
            'None (0x4)': 0x4,
            'Right-Up (0x5)': 0x5,
            'Left-Down (0x6)': 0x6,
            'Down (0x7)': 0x7,
            'Right-Down (0x8)': 0x8,
        })

        self.left_eye_rotation_percent = self.add_float_entry(self.entry_page, 'Left Eye Rotation %')
        self.right_eye_rotation_percent = self.add_float_entry(self.entry_page, 'Right Eye Rotation %')

        self.frames_until_eyes_reach_rotation = self.add_num_entry(self.entry_page, 'Frames until eyes reach rotation')
        self.eye_movement_duration = self.add_num_entry(self.entry_page, 'Eye Movement Duration')
        self.u_16 = self.add_hex_entry(self.unknown_page, 'U_16', max=0xFFFF)

