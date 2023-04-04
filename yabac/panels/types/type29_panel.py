from yabac.panels.types import BasePanel


class Type29Panel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.u_08 = self.add_hex_entry(self.unknown_page, 'U_08')
        self.u_12 = self.add_hex_entry(self.unknown_page, 'U_12')


        self.f_16 = self.add_float_entry(self.unknown_page, 'f_16')
        self.f_20 = self.add_float_entry(self.unknown_page, 'f_20')
        self.f_24 = self.add_float_entry(self.unknown_page, 'f_24')
        self.f_28 = self.add_float_entry(self.unknown_page, 'f_28')
        self.f_32 = self.add_float_entry(self.unknown_page, 'f_32')
        self.f_36 = self.add_float_entry(self.unknown_page, 'f_36')
        self.f_40 = self.add_float_entry(self.unknown_page, 'f_40')
        self.f_44 = self.add_float_entry(self.unknown_page, 'f_44')
        self.f_48 = self.add_float_entry(self.unknown_page, 'f_48')

        self.u_52 = self.add_hex_entry(self.unknown_page, 'u_52')
        self.u_56 = self.add_hex_entry(self.unknown_page, 'u_56')




