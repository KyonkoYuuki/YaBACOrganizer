from yabac.panels.types import BasePanel
from pyxenoverse.bac.types.part_invisibility import PartInvisibility


class PartInvisibilityPanel(BasePanel):
    def __init__(self, *args):
        BasePanel.__init__(self, *args)
        self.bcs_part_id = self.add_single_selection_entry(self.entry_page, 'BCS Part ID', majorDimension=3,
                                                           choices=PartInvisibility.description_choices())

        self.on_off_switch = self.add_single_selection_entry(self.entry_page, 'On/Off Switch', choices={
            'Yes': 0x0,
            'No': 0x1
        })
