from yabac.panels.types import BasePanel


class AuraEffectPanel(BasePanel):
    def __init__(self, *args):
        BasePanel.__init__(self, *args)
        self.aura_type = self.add_single_selection_entry(self.entry_page, 'Type', majorDimension=2, choices={
            'Boost start': 0x0,
            'Boost loop': 0x1,
            'Boost end': 0x2,
            'Ki charge loop': 0x3,
            'Ki charge end': 0x4,
            'Transform aura loop': 0x5,
            'Transform aura end': 0x6
        })
        self.on_off_switch = self.add_single_selection_entry(
            self.entry_page, 'On/Off switch', choices=['Off'], multiple=True)
        self.u_0c = self.add_hex_entry(self.unknown_page, 'U_0C')
