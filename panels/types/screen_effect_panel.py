from yabac.panels.types import BasePanel


class ScreenEffectPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.bpe_effect_id = self.add_num_entry(self.entry_page, 'BPE Effect Id')
        self.u_0c = self.add_hex_entry(self.unknown_page, 'U_0C')
        self.u_10 = self.add_hex_entry(self.unknown_page, 'U_10')
        self.u_14 = self.add_hex_entry(self.unknown_page, 'U_14')
        self.u_18 = self.add_hex_entry(self.unknown_page, 'U_18')
        self.u_1c = self.add_hex_entry(self.unknown_page, 'U_1C')
