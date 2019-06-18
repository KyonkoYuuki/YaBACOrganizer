from yabac.panels.types import Page, BasePanel


class HitboxPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)

        damage_page = Page(self.notebook)
        matrix_page = Page(self.notebook)
        self.notebook.InsertPage(1, damage_page, 'BDM/Damage')
        self.notebook.InsertPage(2, matrix_page, 'Matrix')
        self.bdm_entry = self.add_num_entry(damage_page, 'BDM Entry')
        self.hitbox_flags = self.add_multiple_selection_entry(self.entry_page, 'Hitbox Flags', choices=[
            ('Impact Type', {
                'None': 0x0,
                'Unknown (0x1)': 0x1,
                'Single': 0x2,
                'Unknown (0x4)': 0x4,
            }, False),
            ('Damage Type', {
                'Health': 0x0,
                'No impact (0x1)': 0x1,
                'No damage': 0x2,
                'Ki': 0x4,
                'No impact (0x8)': 0x8
            }, False),
            ('Hitbox Spawn Source', {
                'User': 0x0,
                'Unknown (0x1)': 0x1,
                'Unknown (0x2)': 0x2,
                'Unknown (0x4)': 0x4,
                'Target': 0x8
            }, False),
            ('Unknown', None, True)
        ])
        self.damage = self.add_num_entry(damage_page, 'Damage')
        self.damage_when_blocked = self.add_num_entry(damage_page, 'Damage When Blocked')
        self.stamina_taken_when_blocked = self.add_num_entry(
            damage_page, 'Stamina Taken When Blocked', True)
        self.use_matrix = self.add_single_selection_entry(matrix_page, 'Use Matrix', choices={
            'Off': 0x0,
            'On': 0x1,
            'Unknown (0x2)': 0x2
        })
        self.bdm_type = self.add_single_selection_entry(damage_page, 'BDM Type', choices={
            'CMN.bdm': 0x0,
            'Character': 0x01,
            'Skill': 0x02
        })
        self.u_14 = self.add_hex_entry(self.unknown_page, 'U_14')
        self.u_18 = self.add_hex_entry(self.unknown_page, 'U_18')
        self.position_x = self.add_float_entry(matrix_page, 'Position X')
        self.position_y = self.add_float_entry(matrix_page, 'Position Y')
        self.position_z = self.add_float_entry(matrix_page, 'Position Z')
        self.size_x = self.add_float_entry(matrix_page, 'Size X')
        self.size_y = self.add_float_entry(matrix_page, 'Size Y')
        self.size_z = self.add_float_entry(matrix_page, 'Size Z')
        self.rotation_x = self.add_float_entry(matrix_page, 'Rotation X')
        self.rotation_y = self.add_float_entry(matrix_page, 'Rotation Y')
        self.rotation_z = self.add_float_entry(matrix_page, 'Rotation Z')

