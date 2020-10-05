from yabac.panels.types import BasePanel


class PhysicsPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.function_type = self.add_unknown_hex_entry(self.entry_page, 'Function Type', showKnown=True, knownValues={
            0x0: 'Simulate Physics',
            0x1: 'Play SCD Animations',
        })
        self.ean_index = self.add_num_entry(self.entry_page, 'EAN Index')
        self.u_10 = self.add_hex_entry(self.unknown_page, 'U_10')
        self.f_14 = self.add_float_entry(self.unknown_page, 'F_14')
        self.f_18 = self.add_float_entry(self.unknown_page, 'F_18')
        self.u_1c = self.add_hex_entry(self.unknown_page, 'U_1C')
