from yabac.panels.types import BasePanel, BONE_TYPES


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
            20: 'Ripple Blur',
            21: 'Ripple Blur',
            22: 'Ripple Blur',
            23: 'Ripple Blur',
            24: 'Gravely Blur',
            25: 'Gravely Blur',
            26: 'Ripple Blur ',
            27: 'Ripple Blur',
            30: 'Solar Flare Screen Effect (Opponent Blind)',
            31: 'blackening around the screen',
            32: 'blackening around the screen',
            33: 'Faint Black Circle',
            34: 'A pair of faint Black Circles',
            35: 'faint Black Circle',
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
            66: 'Black Spheres',
            70: 'Standard Black Filter used during Skill Activations'
        }

class ScreenEffectPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.bpe_effect_id = self.add_unknown_num_entry(self.entry_page, 'BPE Effect Id', knownValues=IDs)
        self.bone_link = self.add_single_selection_entry(self.entry_page, 'Bone Link', majorDimension=5, choices=BONE_TYPES)
        self.screeneffect_flags = self.add_multiple_selection_entry(self.entry_page, 'ScreenEffect Flags', majorDimension=2, choices=[
            ('ScreenEffect Options #1', [
                None,
                None,
                None,
                None
            ], True),
            ('ScreenEffect Options #2', [
                None,
                None,
                None,
                None
            ], True),
            ('Activation Options', {
                'On' : 0x0,
                'Unknown (0x1)' : 0x1,
                "Off? (0x2)" : 0x2,
                'Off? (0x3)' : 0x3
            }, False)
        ])


        self.u_10 = self.add_hex_entry(self.unknown_page, 'U_10')
        self.u_14 = self.add_float_entry(self.unknown_page, 'f_14')
        self.u_18 = self.add_float_entry(self.unknown_page, 'f_18')
        self.u_1c = self.add_hex_entry(self.unknown_page, 'U_1C')
