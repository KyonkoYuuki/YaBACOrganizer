from yabac.panels.types import BasePanel, Page, BONE_TYPES


class ProjectilePanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        bsa_page = Page(self.notebook)
        spawn_page = Page(self.notebook)

        self.notebook.InsertPage(1, bsa_page, 'BSA/Skill')
        self.notebook.InsertPage(2, spawn_page, 'Spawn')

        self.skill_id = self.add_num_entry(self.entry_page, 'Skill Id')
        self.can_use_cmn_bsa = self.add_single_selection_entry(bsa_page, 'Can Use CMN BSA', choices={
            'No': 0x0,
            'Yes': 0xffff
        })
        self.projectile_id = self.add_num_entry(bsa_page, 'Projectile Id')
        self.bone_to_spawn_from = self.add_single_selection_entry(
            bsa_page, 'Bone to Spawn From', majorDimension=5, choices=BONE_TYPES)

        self.spawn_source = self.add_multiple_selection_entry(spawn_page, 'Spawn Source', cols=1, majorDimension=3, choices=[
            ('Spawn', {
                'Spawn source': 0x0,
                'Unknown (0x1)': 0x1,
                'User direction': 0x3
            }, False),
            (None, None, False),
            ('Location', {
                'User': 0x0,
                'Target (0x1)': 0x1,
                'Unknown (0x3)': 0x3,
                'Unknown (0x4)': 0x4,
                'Target (0x5)': 0x5,
                'Unknown (0x6)': 0x6,
            }, False)
        ])
        self.position_x = self.add_float_entry(self.entry_page, 'Position X')
        self.position_y = self.add_float_entry(self.entry_page, 'Position Y')
        self.position_z = self.add_float_entry(self.entry_page, 'Position Z')
        self.skill_type = self.add_unknown_hex_entry(self.entry_page, 'Skill Type', showKnown=True, cols=3, knownValues={
            0x0: 'CMN',
            0x3: 'Awoken',
            0x5: 'Super',
            0x6: 'Ultimate',
            0x7: 'Evasive',
            0x8: 'Blast',
        })
        self.spawn_properties = self.add_multiple_selection_entry(spawn_page, 'Spawn Properties', cols=1, choices=[
            ('Duplicate', {
                'None': 0x0,
                'One per player': 0x1,
                'Unknown (0x2)': 0x2
            }, False),
            ('Looping', {
                'Disable': 0x0,
                'Unknown (0x7)': 0x7,
                'Enable': 0x8
            }, False)
        ])
        self.projectile_health = self.add_num_entry(self.entry_page, 'Projectile Health', max=0xFFFFFFFF)
        self.u_20 = self.add_hex_entry(self.unknown_page, 'U_20')
        self.f_28 = self.add_float_entry(self.unknown_page, 'F_28')
        self.u_2e = self.add_hex_entry(self.unknown_page, 'U_2E', max=0xFFFF)
        self.u_34 = self.add_hex_entry(self.unknown_page, 'U_34')
        self.u_38 = self.add_hex_entry(self.unknown_page, 'U_38')
        self.u_3c = self.add_hex_entry(self.unknown_page, 'U_3C')

