from yabac.panels.types import BasePanel, Page


class Type29Panel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)

        #ean_page = Page(self.notebook)
        #self.notebook.InsertPage(1, ean_page, 'Parts')


        self.part_flags = self.add_multiple_selection_entry(self.unknown_page, 'PartFlags', majorDimension=3, choices=[
            (None, None, True),
            (None, None, True),
            (None, None, True),
            (None, None, True),
            ('Part ID', {
                'None?': 0x0,
                'FaceBase': 0x1,
                'FaceForhead': 0x2,
                'FaceEye': 0x3,
                'FaceNose': 0x4,
                'Hair': 0x5,
                'Bust': 0x6,
                'Pants': 0x7,
                'Rist': 0x8,
                'Boots': 0x9
            }, False)
        ])

        self.u_12 = self.add_hex_entry(self.unknown_page, 'U_12')


        self.glare_red_start = self.add_float_entry(self.unknown_page, 'Glare Red (Start)')
        self.glare_green_start = self.add_float_entry(self.unknown_page, 'Glare Green (Start)')
        self.glare_blue_start = self.add_float_entry(self.unknown_page, 'Glare Blue (Start)')
        self.glare_alpha_start = self.add_float_entry(self.unknown_page, 'Glare Alpha (Start)')
        self.glare_red_end = self.add_float_entry(self.unknown_page, 'Glare Red (End)')
        self.glare_green_end = self.add_float_entry(self.unknown_page, 'Glare Green (End)')
        self.glare_blue_end = self.add_float_entry(self.unknown_page, 'Glare Blue (End)')
        self.glare_alpha_end = self.add_float_entry(self.unknown_page, 'Glare Alpha (End)')


        self.f_48 = self.add_float_entry(self.unknown_page, 'f_48')

        self.u_52 = self.add_hex_entry(self.unknown_page, 'u_52')
        self.u_56 = self.add_hex_entry(self.unknown_page, 'u_56')




