from yabac.panels.types import BasePanel


class DualSkillDataPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.u_08 = self.add_hex_entry(self.unknown_page, 'U_08')
        self.u_0a = self.add_hex_entry(self.unknown_page, 'U_0A')
        self.u_0c = self.add_hex_entry(self.unknown_page, 'U_0C')
        self.u_0e = self.add_hex_entry(self.unknown_page, 'U_0E')
        self.u_10 = self.add_hex_entry(self.unknown_page, 'U_10')
        self.f_14 = self.add_hex_entry(self.unknown_page, 'F_14')
        self.f_18 = self.add_hex_entry(self.unknown_page, 'F_18')
        self.f_1c = self.add_hex_entry(self.unknown_page, 'F_1C')
        self.u_20 = self.add_hex_entry(self.unknown_page, 'U_20')
        self.u_22 = self.add_hex_entry(self.unknown_page, 'U_22')
        self.u_24 = self.add_hex_entry(self.unknown_page, 'U_24')
        self.f_28 = self.add_hex_entry(self.unknown_page, 'F_28')
        self.f_2c = self.add_hex_entry(self.unknown_page, 'F_2C')
        self.f_30 = self.add_hex_entry(self.unknown_page, 'F_30')
        self.u_34 = self.add_hex_entry(self.unknown_page, 'U_34')
        self.u_36 = self.add_hex_entry(self.unknown_page, 'U_36')
