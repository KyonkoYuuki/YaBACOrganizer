from yabac.panels.types import BasePanel, Page, BONE_TYPES


class ThrowHandlerPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        bone_page = Page(self.notebook)
        self.notebook.InsertPage(1, bone_page, 'Bone')
        self.throw_flags = self.add_hex_entry(self.entry_page, 'Throw Flags', max=0xFFFF)
        self.u_0a = self.add_hex_entry(self.unknown_page, 'U_0A')
        self.bone_user_connects_to_victim_from = self.add_single_selection_entry(
            bone_page, 'Bone User Connects\nto Victim From', majorDimension=5, choices=BONE_TYPES)
        self.bone_victim_connects_to_user_from = self.add_single_selection_entry(
            bone_page, 'Bone Victim Connects\nto User From', majorDimension=5, choices=BONE_TYPES)
        self.bac_entry = self.add_num_entry(self.entry_page, 'BAC Entry')
        self.u_12 = self.add_hex_entry(self.unknown_page, 'U_12')
        self.victim_displacement_x = self.add_float_entry(bone_page, 'Victim\nDisplacement X')
        self.victim_displacement_y = self.add_float_entry(bone_page, 'Victim\nDisplacement Y')
        self.victim_displacement_z = self.add_float_entry(bone_page, 'Victim\nDisplacement Z')
