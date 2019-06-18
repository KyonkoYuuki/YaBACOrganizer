from yabac.panels.types import BasePanel, Page, BONE_TYPES


class CameraPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        ean_page = Page(self.notebook)
        info_page = Page(self.notebook)
        self.notebook.InsertPage(1, ean_page, 'EAN/Bone')
        self.notebook.InsertPage(2, info_page, 'Info')

        self.ean_type = self.add_single_selection_entry(ean_page, 'EAN Type', majorDimension=3, choices={
            'Basic Lock (0x0)': 0x0,
            'Heavy Rumble (0x1)': 0x1,
            'Extreme Rumble (0x2)': 0x2,
            'CMN.cam.ean': 0x3,
            'Character': 0x4,
            'Skill': 0x5,
            'Unknown (0x6)': 0x6,
            'Static': 0x7,
            'Victim': 0x8,
            'Unknown (0x9)': 0x9,
            'Zoom/speed lines': 0xa,
            'Cinematic (0xb)': 0xb,
            'Cinematic (0xc)': 0xc,
            'Unknown (0xd)': 0xd,
            'Heavy Rumble (0xe)': 0xe,
            'Extreme Rumble (0xf)': 0xf,
        })

        self.bone_to_focus_on = self.add_single_selection_entry(
            ean_page, 'Bone to Focus On', majorDimension=5, choices=BONE_TYPES)
        self.ean_index = self.add_num_entry(ean_page, 'EAN Index')
        self.frame_start = self.add_num_entry(self.entry_page, 'Frame Start')
        self.u_10 = self.add_hex_entry(self.unknown_page, 'U_10', max=0xFFFF)
        self.u_12 = self.add_hex_entry(self.unknown_page, 'U_12', max=0xFFFF)
        self.x_position = self.add_float_entry(info_page, 'X Position')
        self.y_position = self.add_float_entry(info_page, 'Y Position')
        self.z_position = self.add_float_entry(info_page, 'Z Position')
        self.x_rotation = self.add_float_entry(info_page, 'X Rotation')
        self.y_rotation = self.add_float_entry(info_page, 'Y Rotation')
        self.z_rotation = self.add_float_entry(info_page, 'Z Rotation')
        self.x_z_disposition = self.add_float_entry(info_page, 'X/Z Disposition')
        self.y_z_disposition = self.add_float_entry(info_page, 'Y/Z Disposition')
        self.zoom = self.add_float_entry(info_page, 'Zoom')

        self.u_38 = self.add_hex_entry(self.unknown_page, 'U_38')
        self.u_3c = self.add_hex_entry(self.unknown_page, 'U_3C')
        self.u_40 = self.add_hex_entry(self.unknown_page, 'U_40')
        self.u_44 = self.add_hex_entry(self.unknown_page, 'U_44')
        self.u_48 = self.add_hex_entry(self.unknown_page, 'U_48', max=0xFFFF)
        self.camera_flags = self.add_multiple_selection_entry(self.entry_page, 'Camera Flags', choices=[
            ('Unknown', None, True),
            ('Position/rotation/zoom', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Don't override target camera",
                'Enabled'
            ], True),
            ('Additional flags', [
                'Force all players',
                'Unknown (0x2)',
                'Focus on target',
                'Force character cam.ean'
            ], True)
        ])

