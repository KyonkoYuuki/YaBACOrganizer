from yabac.panels.types import BasePanel

IDs={
            0: 'Brightens up the screen',
            1: 'White Screen',
            2: 'Brightens up the screen',
            3: 'Quick White Flash',
            4: 'Brightness Wavering',
            5: 'Red Tint',
            6: 'Fast Brightness Wavering',
            10: 'Small Motion Blur',
            11: 'Strong Motion Blur',
            12: 'Quick Motion Blur,',
            13: 'Very Small Motion Blur',
            14: 'Light Blue Filter',
            15: 'Quick Motion Blur',
            16: 'Quick Motion Blur',
            17: 'Magenta Filter',
            18: 'Two Different Motion Blurs',
            20: 'Ripple Blur on Right Fist',
            21: 'Ripple Blur on Right Fist',
            22: 'Ripple Blur on Right Fist',
            23: 'Ripple Blur over Character’s Head',
            24: 'Gravely Blur on Right Fist',
            25: 'Gravely Blur on Right Fist',
            26: 'Ripple Blur over Character',
            27: 'Ripple Blur over Character',
            30: 'Solar Flare Screen Effect (Opponent Blind)',
            31: 'blackening around the screen',
            32: 'blackening around the screen',
            33: 'Faint Black Circle around the character',
            34: 'A pair of faint Black Circles',
            35: 'aint Black Circle',
            36: 'Solar Flare Screen Effect (User Activate)',
            37: 'Screen turns completely black',
            40: 'Small Transparent Ring expanding',
            41: 'Transparent Ring',
            42: 'Transparent Ring',
            43: 'Big Transparent Ring',
            44: 'Big Transparent Ring',
            45: 'Big Transparent Ring',
            46: 'Transparent Ring',
            50: 'Brightening of the Screen',
            51: 'Brightening of the Screen',
            52: 'Big Transparent Ring',
            53: 'Blue Tint',
            54: 'blackening around the screen',
            55: 'Screen slightly darkens and desaturates',
            56: 'Screen slightly darkens and desaturates',
            57: 'Screen slightly darkens and desaturates',
            60: 'Screen flashes a faint white',
            61: 'Screen slightly darkens and desaturates',
            63: 'Screen slightly darkens and desaturates',
            64: 'Screen flashes a faint pink for a second',
            65: 'Light Blue Filter Fades in and out',
            66: 'Black Spheres the character',
            70: 'Standard Black Filter used during Skill Activations'
        }

class ScreenEffectPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.bpe_effect_id = self.add_unknown_num_entry(self.entry_page, 'BPE Effect Id', knownValues=IDs)
        self.u_0c = self.add_multiple_selection_entry(self.entry_page, 'ScreenEffect Flags', choices=[
            ('ScreenEffect Options #1', [
                'Flag effect to not expire',
                'Force expire effect',
                "Unknown (0x4)",
                'Unknown (0x8)'
            ], True),
            ('ScreenEffect Options #2', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Unknown (0x4)",
                'Unknown (0x8)'
            ], True),
            ('ScreenEffect Options #3', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Unknown (0x4)",
                'Unknown (0x8)'
            ], True),
            ('ScreenEffect Options #4', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Unknown (0x4)",
                'Unknown (0x8)'
            ], True),
            ('ScreenEffect Options #5', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Unknown (0x4)",
                'Unknown (0x8)'
            ], True)
        ])
        self.u_10 = self.add_hex_entry(self.unknown_page, 'U_10')
        self.u_14 = self.add_hex_entry(self.unknown_page, 'U_14')
        self.u_18 = self.add_hex_entry(self.unknown_page, 'U_18')
        self.u_1c = self.add_hex_entry(self.unknown_page, 'U_1C')
