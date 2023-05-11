from yabac.panels.types import BasePanel


class Type30Panel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)





        self.type30_duration = self.add_float_entry(self.entry_page, 'Duration?')
        self.u_12 = self.add_hex_entry(self.unknown_page, 'U_12')
        self.u_16 = self.add_hex_entry(self.unknown_page, 'U_16')
        self.u_20 = self.add_hex_entry(self.unknown_page, 'U_20')
        self.u_24 = self.add_hex_entry(self.unknown_page, 'U_24')
        self.u_28 = self.add_hex_entry(self.unknown_page, 'U_28')
        self.u_32 = self.add_hex_entry(self.unknown_page, 'U_32')
        self.u_36 = self.add_hex_entry(self.unknown_page, 'U_36')
        self.u_40 = self.add_hex_entry(self.unknown_page, 'U_40')
        self.u_44 = self.add_hex_entry(self.unknown_page, 'U_44')




