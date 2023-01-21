from yabac.panels.types import BasePanel
from pyxenoverse.bac.types.sound import Sound


class SoundPanel(BasePanel):
    def __init__(self, *args):
        BasePanel.__init__(self, *args)
        self.acb_type = self.add_single_selection_entry(self.entry_page, 'ACB Type', majorDimension=4,
                                                        choices=Sound.description_choices())

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
                'Stop VOX on matching ID',
                "Pitch and Reverb",
                'Stop when BAC entry is exited'
            ], True)
        ])

        self.u_0e = self.add_hex_entry(self.unknown_page, 'U_0E', max=0xFFFF)
