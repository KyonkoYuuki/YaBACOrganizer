from yabac.panels.types import BasePanel


class PartInvisibilityPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.bcs_part_id = self.add_single_selection_entry(self.entry_page, 'BCS Part ID', majorDimension=3, choices={
            'Face base': 0x0,
            'Face forehead': 0x1,
            'Face eye': 0x2,
            'Face nose ': 0x3,
            'Face ear': 0x4,
            'Hair': 0x5,
            'Bust': 0x6,
            'Pants': 0x7,
            'Rist': 0x8,
            'Boots': 0x9,
        })

        self.on_off_switch = self.add_single_selection_entry(self.entry_page, 'On/Off Switch', choices={
            'Yes': 0x0,
            'No': 0x1
        })
