from pubsub import pub
import wx
from yabac.panels.types import BasePanel, Page
from pyxenoverse.bac.types.homing_movement import HomingMovement


class HomingMovementPanel(BasePanel):
    def __init__(self, *args):

        BasePanel.__init__(self, *args)
        props_page = Page(self.notebook)
        self.notebook.InsertPage(1, props_page, 'Properties')

        # UNLEASHED: the showKnown buttons don't work, the value set does not save
        self.homing_movement_type = self.add_unknown_hex_entry(self.entry_page, 'Type', showKnown=False,
                                                               knownValues=HomingMovement.description)
        self.horizontal_homing_arc_direction = self.add_unknown_hex_entry(
            self.entry_page,
            'Horizontal Homing\nArc Direction',
            showKnown=False,
            knownValues={
                0x0: 'Right->left',
                0x1: 'Left->right',
                0x7: 'Allow float (Speed Modifier)',
                0x23: 'Allow float (Speed Modifier)'
            })
        self.u_20 = self.add_num_entry(props_page, 'I_20')
        self.u_24 = self.add_num_entry(props_page, 'I_24')

        self.speed_modifier = self.add_float_entry(self.entry_page, 'Speed Modifier / Frame Duration')
        self.frame_threshold = self.add_num_entry(self.entry_page, 'Frame Threshold')
        self.horizontal_direction_modifier = self.add_float_entry(self.entry_page, 'Horizontal Direction\nModifier')
        self.vertical_direction_modifier = self.add_float_entry(self.entry_page, 'Vertical Direction\nModifier')
        self.z_direction_modifier = self.add_float_entry(self.entry_page, 'Z Direction\nModifier')

        self.u_26 = self.add_hex_entry(self.unknown_page, 'U_26')
        self.u_28 = self.add_hex_entry(self.unknown_page, 'U_28')
        self.u_2c = self.add_hex_entry(self.unknown_page, 'U_2C')

    def save_entry(self, _):
        self.edit_thread = None
        if self.entry is None:
            return

        start_time = self.entry.start_time
        homing_movement_type_tmp = self.entry.homing_movement_type

        horizontal_homing_arc_direction = self.horizontal_homing_arc_direction.GetValue()
        for name in self.entry.__fields__:
            control = self[name]
            # SpinCtrlDoubles suck
            if isinstance(control, wx.SpinCtrlDouble):
                try:
                    self.entry[name] = float(control.Children[0].GetValue())
                except ValueError:
                    # Keep old value if its mistyped
                    pass
                if name == "speed_modifier" and (horizontal_homing_arc_direction != 7
                                                 and horizontal_homing_arc_direction != 35):
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
