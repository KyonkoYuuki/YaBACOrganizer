from yabac.panels.types import BasePanel
from pyxenoverse.bac.types.aura_effect import AuraEffect


class AuraEffectPanel(BasePanel):
    def __init__(self, *args):
        BasePanel.__init__(self, *args)
        self.aura_type = self.add_single_selection_entry(self.entry_page, 'Type', majorDimension=2,
                                                         choices=AuraEffect.description_choices())
        self.on_off_switch = self.add_single_selection_entry(
            self.entry_page, 'On/Off switch', choices=['Off'], multiple=True)
        self.u_0c = self.add_hex_entry(self.unknown_page, 'U_0C')
