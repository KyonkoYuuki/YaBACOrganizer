from yabac.panels.types import BasePanel


class TrackingPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.tracking = self.add_float_entry(self.entry_page, 'Tracking %')

        self.u_0c = self.add_multiple_selection_entry(self.entry_page, 'Tracking Flags', choices=[
            ('Tracking Options #1', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Track Both Forwards and Backwards",
                'Unknown (0x8)'
            ], True),
            ('Tracking Options #2', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Unknown (0x4)",
                'Unknown (0x8)'
            ], True),
            ('Tracking Options #3', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Unknown (0x4)",
                'Unknown (0x8)'
            ], True)
        ])
        self.u_0e = self.add_hex_entry(self.unknown_page, 'U_0E')
