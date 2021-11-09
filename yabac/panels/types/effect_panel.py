from yabac.panels.types import BasePanel, Page, BONE_TYPES


class EffectPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        eepk_page = Page(self.notebook)

        self.notebook.InsertPage(1, eepk_page, 'Spawn/Bone')
        self.eepk_type = self.add_single_selection_entry(self.entry_page, 'EEPK Type', majorDimension=3, choices={
            'Global': 0x0,
            'Stage BG': 0x1,
            'Player': 0x2,
            'Awoken': 0x3,
            'Super': 0x5,
            'Ultimate': 0x6,
            'Evasive': 0x7,
            'Unknown (0x8)': 0x8,
            'Ki blast': 0x9,
            'Unknown (0xa)': 0xa,
            'Stage (0xb)': 0xb,
        })

        self.bone_link = self.add_single_selection_entry(eepk_page, 'Bone Link', majorDimension=5, choices=BONE_TYPES)

        self.skill_id = self.add_num_entry(self.entry_page, 'Skill Id')
        self.use_skill_id = self.add_single_selection_entry(self.entry_page, 'Use Skill Id', choices={
            'Yes': 0x0,
            'No': 0xffff
        })

        self.effect_id = self.add_num_entry(self.entry_page, 'Effect Id')
        self.position_x = self.add_float_entry(eepk_page, 'Position X')
        self.position_y = self.add_float_entry(eepk_page, 'Position Y')
        self.position_z = self.add_float_entry(eepk_page, 'Position Z')
        self.rotation_x = self.add_float_entry(eepk_page, 'Rotation X')
        self.rotation_y = self.add_float_entry(eepk_page, 'Rotation Y')
        self.rotation_z = self.add_float_entry(eepk_page, 'Rotation Z')
        self.on_off_switch = self.add_unknown_hex_entry(
            self.entry_page, 'On/Off switch', knownValues={
                0x0: 'On',
                0x1: 'Off',
                0x2: 'On',
                0x3: 'Off',
                0x4: 'On (Spawn on target)',
                0x8: 'On (Loop)',
                0x9: 'Off',
                0x10: 'On (Show only to user)',
                0x14: 'On (Spawn on target)',
                0x15: 'Off (used with 0x14)'
            })
