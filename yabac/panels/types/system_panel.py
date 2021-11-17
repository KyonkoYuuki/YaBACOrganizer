from yabac.panels.types import BasePanel
from pyxenoverse.bac.types.system import FUNCTION_MAPPINGS, System

MAPPING_NAMES = ['f_0c', 'f_10', 'f_14', 'f_18', 'f_1c']


class SystemPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.u_0a = self.add_hex_entry(self.unknown_page, 'U_0A')
        # TODO: Make this into a hex control
        self.function_type = self.add_unknown_hex_entry(
            self.entry_page, 'Function', max=0xFF, knownValues=System.description)
        self.f_0c_label, self.f_0c = self.add_nameable_float_entry(self.entry_page, name='F_0C')
        self.f_10_label, self.f_10 = self.add_nameable_float_entry(self.entry_page, name='F_10')
        self.f_14_label, self.f_14 = self.add_nameable_float_entry(self.entry_page, name='F_14')
        self.f_18_label, self.f_18 = self.add_nameable_float_entry(self.entry_page, name='F_18')
        self.f_1c_label, self.f_1c = self.add_nameable_float_entry(self.entry_page, name='F_1C')

        # self.u_18 = self.add_float_entry(self.unknown_page, 'F_18')
        # self.u_1c = self.add_float_entry(self.unknown_page, 'F_1C')

    def load_entry(self, e, entry):
        super().load_entry(e, entry)
        self.calculate_type()

    def save_entry(self, e):
        super().save_entry(e)
        self.calculate_type()

    def calculate_type(self):
        if 'function_type' not in self.__dict__:
            return
        value = self.function_type.GetValue()
        entry = FUNCTION_MAPPINGS.get(value, (None, None, None, None, None, None))

        for i, text in enumerate(entry[1:]):
            if not text and entry[0]:
                self.hide_entry(MAPPING_NAMES[i])
                continue
            if not text:
                text = MAPPING_NAMES[i].upper()
            self.show_entry(MAPPING_NAMES[i], text, 0.0)
