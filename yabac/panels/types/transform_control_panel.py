from yabac.panels.types import BasePanel

mapping_names = ['f_0c', 'f_10', 'f_14']
mappings = {
    0x2: ('Damage', None, None),
    0x4: ('Ki', None, None),
    0x7: ('Y-axisDegrees', None, None),
    0xf: ('Damage', None, None),
    0x10: ('Projectile ID', None, None),
    0x13: ('Partset ID', None, None),
    0x14: ('Partset ID', None, None),
    0x16: ('Stamina', None, None),
    0x1d: ('BAC Entry ID', None, None),
    0x25: ('BAC Entry ID', 'Skill Type', 'Skill ID'),
    0x26: ('BSA Condition', 'Skill Type', 'Skill ID'),
    0x2a: ('Bonescale ID', None, None),
    0x2d: ('Unknown', None, None),
    0x2e: ('Unknown', None, None),
    0x31: ('Health', None, None),
    0x3c: ('Pause Length', None, None),
    0x43: ('Stamina cost', None, None),
    0x44: ('Damage', None, None),
}

MAPPINGS = {
    0x0: ('Loop', None, None, None),
    0x2: ('Damage', 'Damage', None, None),
    0x4: ('Give/take Ki', 'Ki', None, None),
    0x6: ('Invisibility', None, None, None),
    0x7: ('Rotate animation', 'Y-axis Degrees', None, None),
    0xc: ('Darken Screen', None, None, None),
    0xd: ('Activate transformation', None, None, None),
    0xe: ('Deactivate transformation', None, None, None),
    0xf: ('Damage user once', None, None, None),
    0x10: ('Projectile type', 'Projectile Id', None, None),
    0x11: ('Swap bodies', None, None, None),
    0x12: ('Target/untarget', None, None, None),
    0x13: ('Set BCS Part', 'Partset Id', None, None),
    0x14: ('Set BCS Part', 'Partset Id', None, None),
    0x15: ('Remove user', None, None, None),
    0x16: ('Give/take stamina', None, None, None),
    0x1b: ('Limited transformation', None, None, None),
    0x1d: ('Go to entry', 'BAC Entry', None, None),
    0x1f: ('Reset Camera', None, None, None),
    0x20: ('Disable movement/skill', None, None, None),
    0x22: ('Loop (held down)', None, None, None),
    0x23: ('Floating rocks', None, None, None),
    0x24: ('Knock away rocks', None, None, None),
    0x25: ('Go to entry at end', 'BAC Entry ID', 'Skill Type', 'Skill Id'),
    0x26: ('Change projectile', 'BSA Condition', 'Skill Type', 'Skill Id'),
    0x28: ('Invisible opponents', None, None, None),
    0x29: ('Untargetable player', None, None, None),
    0x2a: ('BCS Bonescale', 'Bonescale Id', None, None),
    0x2d: ('No-clip', 'Unknown', None, None),
    0x2e: ('Big collision box', 'Unknown', None, None),
    0x30: ('Black void', None, None, None),
    0x31: ('Regen health', 'Health', None, None),
    0x3c: ('Freeze user', 'Pause Length', None, None),
    0x3f: ('Limit burst', None, None, None),
    0x43: ('Auto-dodge', 'Stamina cost', None, None),
    0x44: ('Damage x10', 'Damage', None, None),
}


class TransformControlPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.u_0a = self.add_hex_entry(self.unknown_page, 'U_0A')
        # TODO: Make this into a hex control
        self.type = self.add_unknown_hex_entry(
            self.entry_page, 'Type', max=0xFF, knownValues={key: value[0] for key, value in MAPPINGS.items()})
        self.f_0c_label, self.f_0c = self.add_nameable_float_entry(self.entry_page, name='F_0C')
        self.f_10_label, self.f_10 = self.add_nameable_float_entry(self.entry_page, name='F_10')
        self.f_14_label, self.f_14 = self.add_nameable_float_entry(self.entry_page, name='F_14')
        self.u_18 = self.add_hex_entry(self.unknown_page, 'U_18')
        self.u_1c = self.add_hex_entry(self.unknown_page, 'U_1C')

    def load_entry(self, e, entry):
        super().load_entry(e, entry)
        self.calculate_type()

    def save_entry(self, e):
        super().save_entry(e)
        self.calculate_type()

    def calculate_type(self):
        if 'type' not in self.__dict__:
            return
        value = self.type.GetValue()
        if value in MAPPINGS:
            entry = MAPPINGS[value]
        else:
            entry = (None, None, None, None)

        for i, text in enumerate(entry[1:]):
            if not text and entry[0]:
                self.hide_entry(mapping_names[i])
                continue
            if not text:
                text = mapping_names[i].upper()
            self.show_entry(mapping_names[i], text, 0.0)
