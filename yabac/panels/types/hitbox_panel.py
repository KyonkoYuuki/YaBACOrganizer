import wx
from yabac.panels.types import Page, BasePanel, BONE_TYPES
from pyxenoverse.bac.types.hitbox import Hitbox


class HitboxPanel(BasePanel):
    def __init__(self, *args):
        BasePanel.__init__(self, *args)

        damage_page = Page(self.notebook)
        matrix_page = Page(self.notebook)
        self.notebook.InsertPage(1, damage_page, 'BDM/Damage')
        self.notebook.InsertPage(2, matrix_page, 'Matrix')
        self.bdm_entry = self.add_num_entry(damage_page, 'BDM Entry')
        self.hitbox_flags = self.add_multiple_selection_entry(
            self.entry_page, 'Hitbox Flags',
            orient=wx.VERTICAL,
            cols=2,
            majorDimension=2,
            choices=[
                ('Impact Type', {
                    'Continuous / None': 0x0,
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

        self.hitbox_properties_1 = self.add_multiple_selection_entry(
            self.entry_page,
            'Hitbox Properties 1',
            majorDimension=2,
            choices=[
                ('Hitbox Options #1', [
                    'Unknown (0x1)',
                    'Unknown (0x2)',
                    "Unknown (0x4)",
                    'Unknown (0x8)'
                ], True),
                ('Hitbox Options #2', [
                    'Unknown (0x1)',
                    'Unknown (0x2)',
                    "Unknown (0x4)",
                    'Unknown (0x8)'
                ], True),
                ('Hitbox Options #3', [
                    'Unknown (0x1)',
                    'Unknown (0x2)',
                    "Unknown (0x4)",
                    'Unknown (0x8)'
                ], True),
                ('Hitbox Options #4', [
                    'Unknown (0x1)',
                    'Unknown (0x2)',
                    "Unknown (0x4)",
                    'Unknown (0x8)'
                ], True)
            ])

        self.bone_link = self.add_single_selection_entry(self.entry_page, 'Bone Link', majorDimension=5, choices=BONE_TYPES)

        self.damage = self.add_num_entry(damage_page, 'Damage')
        self.damage_when_blocked = self.add_num_entry(damage_page, 'Damage When Blocked')
        self.stamina_taken_when_blocked = self.add_num_entry(
            damage_page, 'Stamina Taken When Blocked', True)
        self.matrix_flags = self.add_multiple_selection_entry(matrix_page, 'Matrix Flags', choices=[
            ('Matrix Properties #1', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Unknown (0x4)",
                'Unknown (0x8)'
            ], True),
            ('Matrix Properties #2', [
                'Enable Min and Max bounds',
                'Unknown (0x2)',
                "Unknown (0x4)",
                'Unknown (0x8)'
            ], True)
        ])
        self.bdm_type = self.add_single_selection_entry(damage_page, 'BDM Type', choices=Hitbox.description_choices())

        self.position_x = self.add_float_entry(matrix_page, 'Position X')
        self.position_y = self.add_float_entry(matrix_page, 'Position Y')
        self.position_z = self.add_float_entry(matrix_page, 'Position Z')
        self.scale = self.add_float_entry(matrix_page, 'Scale')
        self.maximum_box_x = self.add_float_entry(matrix_page, 'Maximum Box X')
        self.maximum_box_y = self.add_float_entry(matrix_page, 'Maximum Box Y')
        self.maximum_box_z = self.add_float_entry(matrix_page, 'Maximum Box Z')
        self.minimum_box_x = self.add_float_entry(matrix_page, 'Minimum Box X')
        self.minimum_box_y  = self.add_float_entry(matrix_page, 'Minimum Box Y')
        self.minimum_box_z  = self.add_float_entry(matrix_page, 'Minimum Box Z')
