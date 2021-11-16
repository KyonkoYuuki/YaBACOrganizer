from yabac.panels.types import BasePanel, Page, BONE_TYPES


class CameraPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        ean_page = Page(self.notebook)
        info_page = Page(self.notebook)
        interpolation_page = Page(self.notebook)
        self.notebook.InsertPage(1, ean_page, 'EAN/Bone')
        self.notebook.InsertPage(2, info_page, 'Offsets')
        self.notebook.InsertPage(3, interpolation_page, 'Interpolation')

        self.ean_type = self.add_single_selection_entry(ean_page, 'EAN Type', majorDimension=3, choices={
            'Rumble (0x0)': 0x0,
            'Heavy Rumble (0x1)': 0x1,
            'Extreme Rumble (0x2)': 0x2,
            'CMN.cam.ean': 0x3,
            'Character': 0x4,
            'Skill': 0x5,
            'Zoom': 0x6,
            'Static': 0x7,
            'Victim': 0x8,
            'Unknown (0x9)': 0x9,
            'Zoom/speed lines': 0xa,
            'Cinematic (0xb)': 0xb,
            'Cinematic (0xc)': 0xc,
            'Unknown (0xd)': 0xd,
            'Heavy Rumble (0xe)': 0xe,
            'Extreme Rumble (0xf)': 0xf,
            'Zoom into player (0x11)': 0x11,
            'Unknown (0x14)': 0x14,
            'Unknown (0x16)': 0x16,
            'Activate Extended Camera (0x19)': 0x19,
            'Unknown (0x1A)': 0x1A,
            'Deactivate Extended Camera (0x20)': 0x20,
        })

        self.bone_to_focus_on = self.add_single_selection_entry(
            ean_page, 'Bone to Focus On', majorDimension=5, choices=BONE_TYPES)
        self.ean_index = self.add_num_entry(ean_page, 'EAN Index')
        self.frame_start = self.add_num_entry(self.entry_page, 'Frame Start')
        self.u_10 = self.add_hex_entry(self.unknown_page, 'U_10', max=0xFFFF)

        self.x_position = self.add_float_entry(info_page, 'X Position')
        self.y_position = self.add_float_entry(info_page, 'Y Position')
        self.z_position = self.add_float_entry(info_page, 'Z Position')
        self.x_rotation = self.add_float_entry(info_page, 'X Rotation')
        self.y_rotation = self.add_float_entry(info_page, 'Y Rotation')
        self.z_rotation = self.add_float_entry(info_page, 'Z Rotation')
        self.x_z_disposition = self.add_float_entry(info_page, 'X/Z Disposition')
        self.y_z_disposition = self.add_float_entry(info_page, 'Y/Z Disposition')
        self.zoom = self.add_float_entry(info_page, 'Zoom')

        self.x_position_duration = self.add_num_entry(interpolation_page, 'X Position Duration')
        self.y_position_duration = self.add_num_entry(interpolation_page, 'Y Position Duration')
        self.z_position_duration = self.add_num_entry(interpolation_page, 'Z Position Duration')


        self.x_rotation_duration = self.add_num_entry(interpolation_page, 'X Rotation Duration')
        self.y_rotation_duration = self.add_num_entry(interpolation_page, 'Y Rotation Duration')
        self.z_rotation_duration = self.add_num_entry(interpolation_page, 'Z Rotation Duration')

        self.zoom_duration = self.add_num_entry(interpolation_page, 'Zoom Duration')
        self.displacement_xz_duration = self.add_num_entry(interpolation_page, 'Displacement X/Z Duration')
        self.displacement_yz_duration = self.add_num_entry(interpolation_page, 'Displacement Y/Z Duration')
        self.duration_all = self.add_num_entry(interpolation_page, 'Duration ALL')
        self.camera_flags = self.add_multiple_selection_entry(self.entry_page, 'Camera Flags', choices=[
            ('ECC Options', None, True),
            ('View', [
                'Disable Photo Mode',
                'Snap to View',
                "Move to View",
                'Unknown (0x8)'
            ], True),
            ('Conditons', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Only play on Knockback",
                'Enable offset changes'
            ], True),
            ('Camera Playback', [
                'Force all players to watch',
                'Unknown (0x2)',
                'Play relative to target',
                'Force character cam.ean'
            ], True)
        ])

