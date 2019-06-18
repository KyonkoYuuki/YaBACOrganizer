from yabac.panels.types import BasePanel, Page


class AnimationPanel(BasePanel):
    def __init__(self, *args):
        BasePanel.__init__(self, *args)
        speed_page = Page(self.notebook)

        self.notebook.InsertPage(1, speed_page, 'Speed')

        self.ean_type = self.add_single_selection_entry(self.entry_page, 'EAN Type', majorDimension=4, choices={
            'CMN.ean': 0x0,
            'Unknown (0x1)': 0x1,
            'Unknown (0x2)': 0x2,
            'Char. EAN': 0x5,
            'Unknown (0x6)': 0x6,
            'CMN.tal.ean (tail)': 0x9,
            'Char. fce.ean (mouth)': 0xa,
            'Char. fce.ean (eye)': 0xb,
            'Unknown (0x28)': 0x28,
            'Unknown (0x29)': 0x29,
            'Unknown (0x2a)': 0x2a,
            'Unknown (0x2b)': 0x2b,
            'Skill Ean': 0xfffe
        })
        self.ean_index = self.add_num_entry(self.entry_page, 'EAN Index')
        self.u_0c = self.add_hex_entry(self.unknown_page, 'U_0C', max=0xFFFF)
        self.u_0e = self.add_hex_entry(self.unknown_page, 'U_0E', max=0xFFFF)
        self.frame_start = self.add_num_entry(self.entry_page, 'Frame Start')
        self.frame_end = self.add_num_entry(self.entry_page, 'Frame End')
        self.frame_loop_start = self.add_num_entry(self.entry_page, 'Frame Loop Start')
        self.u_16 = self.add_hex_entry(self.unknown_page, 'U_16', max=0xFFFF)
        self.speed = self.add_float_entry(speed_page, 'Speed')
        self.transitory_animation_connection_type = self.add_float_entry(
            speed_page, 'Transitory Animation\nConnection Type')
        self.transitory_animation_compression = self.add_float_entry(
            speed_page, 'Transitory Animation\nCompression')


