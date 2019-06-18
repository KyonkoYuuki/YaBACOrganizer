from yabac.panels.types import BasePanel


class ChainAttackParametersPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.u_08 = self.add_hex_entry(self.unknown_page, 'U_08')
        self.total_chain_time = self.add_num_entry(self.entry_page, 'Total Chain Time', True)
        self.u_0e = self.add_hex_entry(self.unknown_page, 'U_0E', max=0xFFFF)
