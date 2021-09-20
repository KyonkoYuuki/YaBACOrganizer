from yabac.panels.types import BasePanel


class DualSkillHandlerPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.u_08 = self.add_multiple_selection_entry(self.entry_page, 'DualSkillHandler Flags', choices=[
            ('DualSkillHandler Options #1', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Track Both Forwards and Backwards",
                'Unknown (0x8)'
            ], True),
            ('DualSkillHandler Options #2', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Unknown (0x4)",
                'Unknown (0x8)'
            ], True),
            ('DualSkillHandler Options #3', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Unknown (0x4)",
                'Unknown (0x8)'
            ], True)
        ])

        self.u_0a = self.add_hex_entry(self.unknown_page, 'U_0A')
        self.u_0c = self.add_hex_entry(self.unknown_page, 'U_0C')
        self.u_0e = self.add_hex_entry(self.unknown_page, 'U_0E')
        self.u_10 = self.add_hex_entry(self.unknown_page, 'U_10')

        self.f_14 = self.add_float_entry(self.entry_page, 'Position Initiator X')
        self.f_18 = self.add_float_entry(self.entry_page, 'Position Initiator Y')
        self.f_1c = self.add_float_entry(self.entry_page, 'Position Initiator Z')

        self.u_20 = self.add_hex_entry(self.unknown_page, 'U_20')
        self.u_22 = self.add_hex_entry(self.unknown_page, 'U_22')
        self.u_24 = self.add_hex_entry(self.unknown_page, 'U_24')

        self.f_28 = self.add_float_entry(self.entry_page, 'Position Partner X')
        self.f_2c = self.add_float_entry(self.entry_page, 'Position Partner Y')
        self.f_30 = self.add_float_entry(self.entry_page, 'Position Partner Z')

        self.u_34 = self.add_hex_entry(self.unknown_page, 'U_34')
        self.u_36 = self.add_hex_entry(self.unknown_page, 'U_36')
