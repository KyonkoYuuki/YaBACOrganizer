from yabac.panels.types import BasePanel


class Type22Panel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.u_08 = self.add_hex_entry(self.unknown_page, 'U_08')
        self.f_0c = self.add_float_entry(self.unknown_page, 'F_0C')
