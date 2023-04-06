from yabac.panels.types import BasePanel


class Type28Panel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)


        self.dyt_flags = self.add_multiple_selection_entry(self.unknown_page, 'DYT Flags?', majorDimension=3, choices=[
            (None, None, True),
            (None, None, True),
            (None, None, True),
            (None, None, True),
            ('Dyt Index', {
                'DATA000?': 0x0,
                'DATA001': 0x1,
                'DATA002': 0x2,
                'DATA003': 0x3,
                'DATA004': 0x4,
                'DATA005': 0x5,
                'DATA006': 0x6,
                'DATA007': 0x7,
                'DATA008': 0x8
            }, False)
        ])


        self.u_040 = self.add_hex_entry(self.unknown_page, 'U_040')
        self.switch_transition_start = self.add_float_entry(self.unknown_page, 'Switch Transition (Start)')
        self.switch_transition_end = self.add_float_entry(self.unknown_page, 'Switch Transition (End)')
        self.u_16 = self.add_hex_entry(self.unknown_page, 'U_16')
        self.u_20 = self.add_hex_entry(self.unknown_page, 'U_20')
        self.u_24 = self.add_hex_entry(self.unknown_page, 'U_24')



