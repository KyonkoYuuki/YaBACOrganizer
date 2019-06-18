from yabac.panels.types import BasePanel


class OpponentKnockbackPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.tracking = self.add_float_entry(self.entry_page, 'Tracking')
        self.u_0c = self.add_hex_entry(self.unknown_page, 'U_0C')
        self.u_0e = self.add_hex_entry(self.unknown_page, 'U_0E')
