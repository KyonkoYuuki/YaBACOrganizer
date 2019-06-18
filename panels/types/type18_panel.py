from yabac.panels.types import BasePanel


class Type18Panel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.u_08 = self.add_hex_entry(self.unknown_page, 'U_08')
        self.u_0c = self.add_hex_entry(self.unknown_page, 'U_0C')
        self.u_10 = self.add_hex_entry(self.unknown_page, 'U_10')
        self.f_14 = self.add_float_entry(self.unknown_page, 'F_14')
        self.f_18 = self.add_float_entry(self.unknown_page, 'F_18')
        self.u_1c = self.add_hex_entry(self.unknown_page, 'U_1C')
