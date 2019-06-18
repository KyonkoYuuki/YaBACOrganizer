from yabac.panels.types import BasePanel


class HomingMovementPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.type = self.add_single_selection_entry(self.entry_page, 'Type', choices={
            'Horizontal arc': 0x0,
            'Straight line': 0x1,
            'Right-left/up-down arc': 0x2
        })
        self.horizontal_homing_arc_direction = self.add_single_selection_entry(
            self.entry_page, 'Horizontal Homing\nArc Direction', majorDimension=5, choices={
                'Right->left': 0x0,
                'Left->right': 0x1,
                'Unknown (0x4)': 0x4,
                'Unknown (0x5)': 0x5,
                'Unknown (0x7)': 0x7,
                'Unknown (0x8)': 0x8,
                'Unknown (0x9)': 0x9,
                'Unknown (0xd)': 0xd,
                'Unknown (0xf)': 0xf,
            })

        self.speed_modifier = self.add_num_entry(self.entry_page, 'Speed Modifier')
        self.u_10 = self.add_hex_entry(self.unknown_page, 'U_10')
        self.horizontal_direction_modifier = self.add_float_entry(self.entry_page, 'Horizontal Direction\nModifier')
        self.vertical_direction_modifier = self.add_float_entry(self.entry_page, 'Vertical Direction\nModifier')
        self.z_direction_modifier = self.add_float_entry(self.entry_page, 'Z Direction\nModifier')
        self.u_20 = self.add_hex_entry(self.unknown_page, 'U_20')
        self.u_24 = self.add_hex_entry(self.unknown_page, 'U_24')
        self.u_28 = self.add_hex_entry(self.unknown_page, 'U_28')
        self.u_2c = self.add_hex_entry(self.unknown_page, 'U_2C')
