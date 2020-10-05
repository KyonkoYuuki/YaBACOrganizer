from yabac.panels.types import BasePanel


class ExtendedCameraControlPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.u_08 = self.add_hex_entry(self.unknown_page, 'U_08')
        self.u_0c = self.add_hex_entry(self.unknown_page, 'U_0C')
        self.u_10 = self.add_hex_entry(self.unknown_page, 'U_10')
        self.u_14 = self.add_hex_entry(self.unknown_page, 'U_14')
        self.u_18 = self.add_hex_entry(self.unknown_page, 'U_18')
        self.u_1c = self.add_hex_entry(self.unknown_page, 'U_1C')
        self.u_20 = self.add_hex_entry(self.unknown_page, 'U_20')
        self.u_24 = self.add_hex_entry(self.unknown_page, 'U_24')
        self.u_28 = self.add_hex_entry(self.unknown_page, 'U_28')
        self.u_2c = self.add_hex_entry(self.unknown_page, 'U_2C')
        self.u_30 = self.add_hex_entry(self.unknown_page, 'U_30')
        self.u_34 = self.add_hex_entry(self.unknown_page, 'U_34')
        self.u_38 = self.add_hex_entry(self.unknown_page, 'U_38')
        self.u_3c = self.add_hex_entry(self.unknown_page, 'U_3C')
        self.u_40 = self.add_hex_entry(self.unknown_page, 'U_40')
        self.u_44 = self.add_hex_entry(self.unknown_page, 'U_44')
        self.u_48 = self.add_hex_entry(self.unknown_page, 'U_48')
        self.u_4c = self.add_hex_entry(self.unknown_page, 'U_4C')
