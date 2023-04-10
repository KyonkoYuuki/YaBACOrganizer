from yabac.panels.types import BasePanel


class BcmCallbackPanel(BasePanel):
    def __init__(self, *args):
        BasePanel.__init__(self, *args)
        self.bcm_link_flags = self.add_multiple_selection_entry(self.entry_page, 'BCM Link Flags', choices=[
            ('Link Options #1', None, True),
            ('Link Options #2', ['Ki blast', 'Jump', 'Guard', 'Step dash/fly'], True),
            ('Link Options #3 / Reciver Link ID', ['Combo', 'Supers', 'Ultimates/Evasives', 'Z-Vanish'], True),
            ('Link Options #4', ['Counters', None, None, 'Back-hit'], True),
            ('Link Options #5', ['Attacks', 'Movement', 'Disable Ki blast', 'No links'], True)
        ])

