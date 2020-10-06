from yabac.panels.types import BasePanel


class BcmCallbackPanel(BasePanel):
    def __init__(self, *args):
        BasePanel.__init__(self, *args)
        self.bcm_link_flags = self.add_multiple_selection_entry(self.entry_page, 'BCM Link Flags', choices=[
            ('', ['Ki blast', 'Jump', 'Guard', 'Step dash/fly'], True),
            ('', ['Combo', 'Supers', 'Ultimates/Evasives', 'Z-Vanish'], True),
            ('', ['Counters', None, None, 'Back-hit'], True),
            ('', ['Attacks', 'Movement', 'Disable Ki blast', 'No links'], True)
        ])
        self.u_0a = self.add_hex_entry(self.unknown_page, 'U_0A', max=0xFFFF)
