from yabac.panels.types import BasePanel, Page


class AnimationPanel(BasePanel):
    def __init__(self, *args):
        BasePanel.__init__(self, *args)
        speed_page = Page(self.notebook)
        flags_page = Page(self.notebook)

        self.notebook.InsertPage(1, speed_page, 'Speed and Transition')
        self.notebook.InsertPage(2, flags_page, 'Flags')

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

        self.animation_flags = self.add_multiple_selection_entry(self.entry_page, 'Animation Flags',  choices=[
            ('Animation Options #1', [
                'Unknown (0x1)',
                'Specific per EAN Type',
                "Unknown (0x4)",
                'Unknown (0x8)'
            ], True),
            ('Animation Options #2', [
                'Unknown (0x1)',
                'Continue From Last Entry',
                "Unknown (0x4)",
                'Unknown (0x8)'
            ], True),
            ('Animation Options #3', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Unknown (0x4)",
                'Unknown (0x8)'
            ], True),
            ('Animation Options #4', [
                'Follow on X Axis',
                'Follow on Y Axis',
                "Follow on Z Axis",
                'Unknown (0x8)'
            ], True)
        ])

        self.play_face_animation_from_skill = self.add_single_selection_entry(flags_page, 'Play Face Animation from Skill / Chara EAN', choices={
            'No': 0x0,
            'Yes': 0x1
        })

        self.ean_index = self.add_num_entry(self.entry_page, 'EAN Index')
        self.frame_start = self.add_num_entry(self.entry_page, 'Frame Start')
        self.frame_end = self.add_num_entry(self.entry_page, 'Frame End')
        self.frame_loop_start = self.add_num_entry(self.entry_page, 'Frame Loop Start')
        self.u_16 = self.add_hex_entry(self.unknown_page, 'U_16', max=0xFFFF)
        self.speed = self.add_float_entry(speed_page, 'Speed')
        self.animation_transition_start_frame = self.add_float_entry(
            speed_page, 'Animation Transition\nStart Frame')
        self.animation_transition_frame_step = self.add_float_entry(
            speed_page, 'Animation Transition\nFrame Step')


