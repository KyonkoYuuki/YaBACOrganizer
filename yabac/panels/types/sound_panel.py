from yabac.panels.types import BasePanel


class SoundPanel(BasePanel):
    def __init__(self, *args):
        BasePanel.__init__(self, *args)
        self.acb_type = self.add_single_selection_entry(self.entry_page, 'ACB Type', majorDimension=4, choices={
            'CAR_BTL_CMN': 0x0,
            'Unknown (0x1)': 0x1,
            'Character SE': 0x2,
            'Character VOX': 0x3,
            'Unknown (0x4)': 0x4,
            'Unknown (0x5)': 0x5,
            'Unknown (0x6)': 0x6,
            'Unknown (0x7)': 0x7,
            'Unknown (0x8)': 0x8,
            'Skill SE': 0xa,
            'Skill VOX': 0xb,
            'Unknown (0x16)': 0x16,
            'Unknown (0x17)': 0x17,
            'Unknown (0x1a)': 0x1a,
            'Unknown (0x1c)': 0x1c,
            'Unknown (0x1d)': 0x1d,
            'Unknown (0x22)': 0x22,
            'Unknown (0x23)': 0x23,
            'Unknown (0x34)': 0x34,
            'Unknown (0x35)': 0x35,
            'Unknown (0x37)': 0x39,
            'Unknown (0x39)': 0x39,
            'Unknown (0x62)': 0x62,
            'Unknown (0x100)': 0x100,
        })

        self.cue_id = self.add_num_entry(self.entry_page, 'Cue ID')

        # TODO: Needs more research
        # self.sound_properties = self.add_single_selection_entry(
        #     self.entry_page, 'Properties', majorDimension=2, choices={
        #         'None': 0x0,
        #         'Play until finished': 0x1,
        #         "Don't play": 0x2,
        #         'Enable Pitch/reverb effects': 0x4,
        #         'Stop when BAC entry ends': 0x8
        # })
        self.sound_flags = self.add_multiple_selection_entry(self.entry_page, 'Sound Flags', choices=[
            ('Sound Options #1', [
                'Mark sound for fade out',
                'Unknown (0x2)',
                "Fade out marked sound",
                'Fade out when skill ends'
            ], True),
            ('Sound Options #2', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Fade out when BAC entry ends",
                'Unknown (0x8)'
            ], True),
            ('Sound Options #3', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Pitch and Reverb",
                'Stop when BAC entry is exited'
            ], True)
        ])

        self.u_0e = self.add_hex_entry(self.unknown_page, 'U_0E', max=0xFFFF)
