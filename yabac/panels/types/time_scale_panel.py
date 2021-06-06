from yabac.panels.types import BasePanel


class TimeScalePanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.time_scale = self.add_float_entry(self.entry_page, 'Time Scale')
