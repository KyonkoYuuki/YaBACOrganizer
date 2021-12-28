from pubsub import pub
import wx
from yabac.panels.types import BasePanel, Page, BONE_TYPES
from pyxenoverse.bac.types.homing_movement import HomingMovement


class HomingMovementPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        bone_link_page = Page(self.notebook)
        self.notebook.InsertPage(1, bone_link_page, 'Bone Link')

        # UNLEASHED: the showKnown buttons don't work, the value set does not save
        self.homing_movement_type = self.add_unknown_hex_entry(self.entry_page, 'Type', showKnown=False,
                                                               knownValues=HomingMovement.description)
        self.properties = self.add_multiple_selection_entry(self.entry_page, 'Properties', choices=[

            ('Options #2', [
                'Unknown (0x1)',
                'Unknown (0x2)',
                "Unknown (0x4)",
                'Unknown (0x8)'
            ], True),
            ('Conditions', [
                'Unknown (0x1)',
                'Enable Float Parameter',
                "Unknown (0x4)",
                'Enable Bone Link'
            ], True),
        ])



        self.u_20 = self.add_single_selection_entry(bone_link_page, 'User Bone', majorDimension=5,
                                                         choices=BONE_TYPES)
        self.u_24 = self.add_single_selection_entry(bone_link_page, 'Target Bone', majorDimension=5,
                                                         choices=BONE_TYPES)

        self.speed_modifier = self.add_float_entry(self.entry_page, 'Speed Modifier / Frame Duration')
        self.frame_threshold = self.add_num_entry(self.entry_page, 'Frame Threshold')
        self.horizontal_direction_modifier = self.add_float_entry(self.entry_page, 'Horizontal Direction\nModifier')
        self.vertical_direction_modifier = self.add_float_entry(self.entry_page, 'Vertical Direction\nModifier')
        self.z_direction_modifier = self.add_float_entry(self.entry_page, 'Z Direction\nModifier')

        self.u_28 = self.add_hex_entry(self.unknown_page, 'U_28')
        self.u_2c = self.add_hex_entry(self.unknown_page, 'U_2C')

    def save_entry(self, _):
        self.edit_thread = None
        if self.entry is None:
            return

        start_time = self.entry.start_time
        homing_movement_type_tmp = self.entry.homing_movement_type

        properties = self.properties.GetValue()
        for name in self.entry.__fields__:
            control = self[name]
            # SpinCtrlDoubles suck
            if isinstance(control, wx.SpinCtrlDouble):
                try:
                    self.entry[name] = float(control.Children[0].GetValue())
                except ValueError:
                    # Keep old value if its mistyped
                    pass
                if name == "speed_modifier" and properties & 2 == 2:
                    old_value, self.entry[name] = self.entry[name], float(self.entry[name])
                    if old_value != self.entry[name]:
                        control.SetValue(self.entry[name])
                elif name == "speed_modifier" and properties & 2 != 2:
                    old_value, self.entry[name] = self.entry[name], int(self.entry[name])
                    if old_value != self.entry[name]:
                        control.SetValue(self.entry[name])
            else:
                self.entry[name] = control.GetValue()

        if self.entry.start_time != start_time:
            pub.sendMessage('update_item', item=self.item, entry=self.entry)
            pub.sendMessage('reindex')

        if self.entry.homing_movement_type != homing_movement_type_tmp:
            pub.sendMessage('reindex')
