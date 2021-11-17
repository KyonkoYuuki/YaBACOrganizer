from yabac.panels.types import BasePanel
from pyxenoverse.bac.types.targeting_assistance import TargetingAssistance


class TargetingAssistancePanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.rotation_axis = self.add_single_selection_entry(
            self.entry_page, 'Rotation Axis', majorDimension=4, choices=TargetingAssistance.description_choices())
        self.u_0a = self.add_hex_entry(self.unknown_page, 'U_0A', max=0xFFFF)
