import wx
from yabac.panels.types import BasePanel


class TrackingPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.tracking = self.add_float_entry(self.entry_page, 'Tracking %')

        self.tracking_flags = self.add_multiple_selection_entry(self.entry_page, 'Tracking Flags' ,orient=wx.VERTICAL, cols=2, majorDimension=2, choices=[
            ('Tracking Options #1', {
                'None': 0x0,
                'Unknown (0x1)' : 0x1,
                'Unknown (0x2)' : 0x2,
                "Unknown (0x3)" : 0x3,
                'Unknown (0x4)' : 0x4
            }, False),
            ('Tracking Options #2', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Track Both Forwards and Backwards",
                'Track Backwards(?)'
            ], True),
            ('Tracking Options #3', [
                None,
                None,
                None,
                None
            ], True),
            ('Tracking Options #4', [
                None,
                None,
                None,
                None
            ], True)
        ])
        self.u_0e = self.add_hex_entry(self.unknown_page, 'U_0E')
