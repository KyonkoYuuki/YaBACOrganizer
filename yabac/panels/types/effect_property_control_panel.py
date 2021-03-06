from yabac.panels.types import BasePanel


class EffectPropertyControlPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.skill_id = self.add_num_entry(self.entry_page, 'Skill Type')
        self.skill_type = self.add_unknown_hex_entry(self.entry_page, 'Skill Type', showKnown=True, cols=3, knownValues={
            0x0: 'CMN',
            0x3: 'Awoken',
            0x5: 'Super',
            0x6: 'Ultimate',
            0x7: 'Evasive',
            0x8: 'Blast',
        })
        self.effect_id = self.add_num_entry(self.entry_page, "Effect ID")
        self.effect_duration = self.add_num_entry(self.entry_page, "Effect Duration")
        self.flags = self.add_unknown_hex_entry(self.entry_page, "Flags")

        self.u_12 = self.add_hex_entry(self.unknown_page, 'U_12')
        self.u_14 = self.add_hex_entry(self.unknown_page, 'U_14')
        self.u_16 = self.add_hex_entry(self.unknown_page, 'U_16')
