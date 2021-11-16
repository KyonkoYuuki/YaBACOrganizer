import wx
from yabac.panels.types import Page, BasePanel


class HitboxPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)

        damage_page = Page(self.notebook)
        matrix_page = Page(self.notebook)
        self.notebook.InsertPage(1, damage_page, 'BDM/Damage')
        self.notebook.InsertPage(2, matrix_page, 'Matrix')
        self.bdm_entry = self.add_num_entry(damage_page, 'BDM Entry')
        self.hitbox_flags = self.add_multiple_selection_entry(self.entry_page, 'Hitbox Flags', orient=wx.VERTICAL, cols=2, majorDimension=2,  choices=[
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

        self.hitbox_properties_1 = self.add_multiple_selection_entry(self.entry_page, 'Hitbox Properties 1', majorDimension=2, choices=[
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

        self.hitbox_properties_2 = self.add_multiple_selection_entry(self.entry_page, 'Hitbox Properties 2', majorDimension=2, choices=[

            ('Hitbox Options #2', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Unknown (0x4)",
                'Unknown (0x8)'
            ], True),
            ('Hitbox Options #1', {
                'None': 0x0,
                'Unknown (0x1)': 0x1,
                'Unknown (0x2)': 0x2,
                "Treat Hitbox as a Sphere": 0x4,
                'Unknown (0x7)': 0x7
            }, False),
        ])


        self.damage = self.add_num_entry(damage_page, 'Damage')
        self.damage_when_blocked = self.add_num_entry(damage_page, 'Damage When Blocked')
        self.stamina_taken_when_blocked = self.add_num_entry(
            damage_page, 'Stamina Taken When Blocked', True)
        self.matrix_flags = self.add_multiple_selection_entry(matrix_page, 'Matrix Flags', choices=[
            ('Matrix Options #1', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Unknown (0x4)",
                'Unknown (0x8)'
            ], True),
            ('Matrix Options #2', [
                'Enable Scale and Rotation',
                'Unknown (0x2)',
                "Unknown (0x4)",
                'Unknown (0x8)'
            ], True)
        ])
        self.bdm_type = self.add_single_selection_entry(damage_page, 'BDM Type', choices={
            'CMN.bdm': 0x0,
            'Character': 0x01,
            'Skill': 0x02
        })




        self.f_18 = self.add_float_entry(self.unknown_page, 'F_18')
        self.position_x = self.add_float_entry(matrix_page, 'Position X')
        self.position_y = self.add_float_entry(matrix_page, 'Position Y')
        self.position_z = self.add_float_entry(matrix_page, 'Position Z')
        self.size_x = self.add_float_entry(matrix_page, 'Size X')
        self.size_y = self.add_float_entry(matrix_page, 'Size Y')
        self.size_z = self.add_float_entry(matrix_page, 'Size Z')
        self.rotation_x = self.add_float_entry(matrix_page, 'Rotation X')
        self.rotation_y = self.add_float_entry(matrix_page, 'Rotation Y')
        self.rotation_z = self.add_float_entry(matrix_page, 'Rotation Z')

