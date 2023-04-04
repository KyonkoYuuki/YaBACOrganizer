from yabac.panels.types import BasePanel


class Type28Panel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.u_00 = self.add_hex_entry(self.unknown_page, 'U_00')
        self.u_040 = self.add_hex_entry(self.unknown_page, 'U_040')
        self.u_08 = self.add_hex_entry(self.unknown_page, 'U_08')
        self.u_12 = self.add_hex_entry(self.unknown_page, 'U_12')
        self.u_16 = self.add_hex_entry(self.unknown_page, 'U_16')
        self.u_20 = self.add_hex_entry(self.unknown_page, 'U_20')
        self.u_24 = self.add_hex_entry(self.unknown_page, 'U_24')



