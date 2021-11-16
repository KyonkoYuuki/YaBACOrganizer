from yabac.panels.types import BasePanel, Page, BONE_TYPES


class ProjectilePanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        bsa_page = Page(self.notebook)
        spawn_page = Page(self.notebook)


        self.notebook.InsertPage(1, bsa_page, 'Bone')
        self.notebook.InsertPage(2, spawn_page, 'Spawn')

        #UNLEASHED: skill type includes extra props
        self.skill_bsa_flags  = self.add_multiple_selection_entry(self.entry_page, 'Skill/BSA Flags',  majorDimension=2,  choices=[
            ('Skill/BSA Options #1', {
                 'None': 0x0,
                 'Terminate Previous Projectile': 0x1,
                 "Unknown (0x2)": 0x2,
                 "Unknown (0x4)": 0x4,
                 "Unknown (0x8)": 0x8
            }, False),
            ('Skill/BSA Options #2', None , True),
            ('Skill Type', {
                'CMN': 0x0,
                'Awoken': 0x3,
                'Super': 0x5,
                'Ultimate': 0x6,
                'Evasive': 0x7,
                'Blast': 0x8
            }, False)
        ])
        self.skill_id = self.add_num_entry(self.entry_page, 'Skill Id')
        self.use_cmn_bsa = self.add_single_selection_entry(self.entry_page, 'Use CMN BSA', choices={
            'No': 0x0,
            'Yes': 0xffff
        })
        self.bsa_id = self.add_num_entry(self.entry_page, 'BSA ID')
        self.bone_to_spawn_from = self.add_single_selection_entry(
            bsa_page, 'Bone to Spawn From', majorDimension=5, choices=BONE_TYPES)

        self.spawn_source = self.add_multiple_selection_entry(spawn_page, 'Spawn Source', cols=1, majorDimension=3, choices=[
            ('Spawn', {
                'Spawn source': 0x0,
                'Unknown (0x1)': 0x1,
                'Unknown (0x2)': 0x2,
                'User direction': 0x3
            }, False),
            (None, None, False),
            ('Location', {
                'User': 0x0,
                'Spawn source (Target) (0x1)': 0x1,
                'Unknown (0x2)': 0x2,
                'Unknown (0x3)': 0x3,
                'User direction (Target)': 0x4,
                'Target (0x5)': 0x5,
                'Unknown (0x6)': 0x6,
                'Map (0x7)': 0x7,
            }, False)
        ])
        self.position_x = self.add_float_entry(spawn_page, 'Position X')
        self.position_y = self.add_float_entry(spawn_page, 'Position Y')
        self.position_z = self.add_float_entry(spawn_page, 'Position Z')
        self.rotation_x = self.add_float_entry(spawn_page, 'Rotation X')
        self.rotation_y  = self.add_float_entry(spawn_page, 'Rotation Y')
        self.rotation_z  = self.add_float_entry(spawn_page, 'Rotation Z')

        # self.spawn_properties = self.add_multiple_selection_entry(spawn_page, 'Spawn Properties', cols=1, choices=[
        #     ('Duplicate', {
        #         'None': 0x0,
        #         'One per player': 0x1,
        #         'Unknown (0x2)': 0x2
        #     }, False),
        #     ('Looping', {
        #         'Disable': 0x0,
        #         'Unknown (0x7)': 0x7,
        #         'Enable': 0x8
        #     }, False)
        # ])
        self.projectile_health = self.add_num_entry(self.entry_page, 'Projectile Health', max=0xFFFFFFFF)
        self.projectile_flags = self.add_multiple_selection_entry(spawn_page, 'Projectile Flags',majorDimension=2, choices=[
            ('Projectile Options #1', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Unknown (0x4)",
                'Unknown (0x8)'
            ], True),
            ('Marking', {
                'None': 0x0,
                'Dupilcate Projectile For Every Opponent': 0x1,
                'Unknown (0x2)': 0x2,
                'Mark Projectile with Random ID': 0x4,
                'Mark Projectile Unique ID (Roster)': 0x8,
                'Mark Projectile Unique ID (CaC)': 0xC
            }, False),
            ('Conditions', [
                'Announce to BCM',
                'Unknown (0x2)',
                "Unknown (0x4)",
                'Enable Loop'
            ], True)
        ])
        self.unique_id = self.add_num_entry(spawn_page, 'Unique ID', max=0xFFFF)
        self.u_38 = self.add_hex_entry(self.unknown_page, 'U_38')
        self.u_3c = self.add_hex_entry(self.unknown_page, 'U_3C')


