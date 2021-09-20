from yabac.panels.types import BasePanel

mapping_names = ['f_0c', 'f_10', 'f_14' ,'f_18' ,'f_1c']
mappings = {
    0x2: ('Damage', None, None, None, None),
    0x4: ('Ki', None, None, None, None),
    0x7: ('Y-axis Degrees', None, None, None, None),
    0xb: ('Duration', None, None, None, None),
    0xf: ('Damage', None, None, None, None),
    0x10: ('BAC Condition', None, None, None, None),
    0x13: ('Partset ID', None, None, None, None),
    0x14: ('Partset ID', None, None, None, None),
    0x16: ('Stamina', None, None, None, None),
    0x1d: ('BAC Entry ID', None, None, None, None),
    0x25: ('BAC Entry ID', 'Skill Type', 'Skill ID', None, None),
    0x26: ('BSA Condition', 'Skill Type', 'Skill ID', None, None),
    0x2a: ('Bonescale ID', None, None, None, None),
    0x2d: ('Unknown', None, None, None, None),
    0x2e: ('Unknown', None, None, None, None),
    0x31: ('Health', None, None, None, None),
    0x3c: ('Pause Length', None, None, None, None),
    0x43: ('Stamina cost', None, None, None, None),
    0x44: ('Damage', None, None, None, None),
    0x4c: ('Super Soul ID', None, None, None, None),
    0x4e: ('Skill Id', 'Skill Type', 'Upgrade Command', None, None)
}

MAPPINGS = {
    0x0: ('Loop', None, None, None, None, None),
    0x2: ('Damage', 'Damage', None, None, None, None),
    0x4: ('Give/take Ki', 'Ki', None, None, None, None),
    0x6: ('Invisibility', None, None, None, None, None),
    0x7: ('Rotate animation', 'Y-axis Degrees', None, None, None, None),
    0xb: ('Override throw duration', 'Duration', None, None, None, None),
    0xc: ('Darken Screen', None, None, None, None, None),
    0xd: ('Activate transformation', None, None, None, None, None),
    0xe: ('Deactivate transformation', None, None, None, None, None),
    0xf: ('Damage user once', None, None, None, None, None),
    0x10: ('Detonate Projectiles', 'BAC Condition', None, None, None, None),
    0x11: ('Swap bodies', None, None, None, None, None),
    0x12: ('Target/untarget', None, None, None, None, None),
    0x13: ('Set BCS Part', 'Partset Id', None, None, None, None),
    0x14: ('Set BCS Part', 'Partset Id', None, None, None, None),
    0x15: ('Remove user', None, None, None, None, None),
    0x16: ('Give/take stamina', 'Stamina', None, None, None, None),
    0x1b: ('Limited transformation', None, None, None, None, None),
    0x1d: ('Go to entry', 'BAC Entry', None, None, None, None),
    0x1f: ('Reset Camera', None, None, None, None, None),
    0x20: ('Disable movement/skill', None, None, None, None, None),
    0x22: ('Loop (held down)', None, None, None, None, None),
    0x23: ('Floating rocks', None, None, None, None, None),
    0x24: ('Knock away rocks', None, None, None, None, None),
    0x25: ('Go to entry at end', 'BAC Entry ID', 'Skill Type', 'Skill Id', None, None),
    0x26: ('Change projectile', 'BSA Condition', 'Skill Type', 'Skill Id', 'F_18', 'F_1C'),
    0x28: ('Invisible opponents', None, None, None, None, None),
    0x29: ('Untargetable player', None, None, None, None, None),
    0x2a: ('BCS Bonescale', 'Bonescale Id', None, None, None, None),
    0x2d: ('No-clip', 'Unknown', None, None, None, None),
    0x2e: ('Big collision box', 'Unknown', None, None, None, None),
    0x30: ('Black void', None, None, None, None, None),
    0x31: ('Regen health', 'Health', None, None, None, None),
    0x3c: ('Stun', 'Stun Duration', None, None, None, None),
    0x3f: ('Limit burst', None, None, None, None, None),
    0x43: ('Auto-dodge', 'Stamina cost', None, None, None, None),
    0x44: ('Damage x10', 'Damage', None, None, None, None),
    0x4c: ('Activate Buff', 'Super Soul ID', None, None, None, None),
    0x4e: ('Skill Upgrade', 'Skill Id', 'Skill Type', 'Upgrade Cmd', 'F_18', 'F_1C')
}


class SystemPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        self.u_0a = self.add_hex_entry(self.unknown_page, 'U_0A')
        # TODO: Make this into a hex control
        self.function_type = self.add_unknown_hex_entry(
            self.entry_page, 'Function', max=0xFF, knownValues={key: value[0] for key, value in MAPPINGS.items()})
        self.f_0c_label, self.f_0c = self.add_nameable_float_entry(self.entry_page, name='F_0C')
        self.f_10_label, self.f_10 = self.add_nameable_float_entry(self.entry_page, name='F_10')
        self.f_14_label, self.f_14 = self.add_nameable_float_entry(self.entry_page, name='F_14')
        self.f_18_label, self.f_18 = self.add_nameable_float_entry(self.entry_page, name='F_18')
        self.f_1c_label, self.f_1c = self.add_nameable_float_entry(self.entry_page, name='F_1C')

        #self.u_18 = self.add_float_entry(self.unknown_page, 'F_18')
        #self.u_1c = self.add_float_entry(self.unknown_page, 'F_1C')

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
        if value in MAPPINGS:
            entry = MAPPINGS[value]
        else:
            entry = (None, None, None, None, None, None)

        for i, text in enumerate(entry[1:]):
            if not text and entry[0]:
                self.hide_entry(mapping_names[i])
                continue
            if not text:
                text = mapping_names[i].upper()
            self.show_entry(mapping_names[i], text, 0.0)
