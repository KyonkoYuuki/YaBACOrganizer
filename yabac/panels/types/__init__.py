import wx
from pubsub import pub
from wx.lib.scrolledpanel import ScrolledPanel

from pyxenoverse.gui import add_entry, EVT_RESULT, EditThread
from pyxenoverse.gui.ctrl.colour_picker_ctrl import ColourPickerCtrl
from pyxenoverse.gui.ctrl.hex_ctrl import HexCtrl
from pyxenoverse.gui.ctrl.multiple_selection_box import MultipleSelectionBox
from pyxenoverse.gui.ctrl.single_selection_box import SingleSelectionBox
from pyxenoverse.gui.ctrl.text_ctrl import TextCtrl
from pyxenoverse.gui.ctrl.unknown_hex_ctrl import UnknownHexCtrl
from pyxenoverse.gui.ctrl.num_ctrl import NumCtrl

MAX_UINT16 = 0xFFFF
MAX_UINT32 = 0xFFFFFFFF
BONE_TYPES = {
    'b_C_Base': 0x0,
    'b_C_Chest': 0x1,
    'b_C_Head': 0x2,
    'b_C_Neck1': 0x3,
    'b_C_Pelvis': 0x4,
    'b_C_Spine1': 0x5,
    'b_C_Spine2': 0x6,
    'b_R_Hand': 0x7,
    'b_L_Hand': 0x8,
    'b_R_Arm': 0x9,
    'b_L_Arm': 0xa,
    'b_R_Shoulder': 0xb,
    'b_L_Shoulder': 0xc,
    'b_R_Foot': 0xd,
    'b_L_Foot': 0xe,
    'b_R_Leg1': 0x0f,
    'b_L_Leg 1': 0x10,
    'g_C_Head': 0x11,
    'g_C_Pelvis': 0x12,
    'g_L_Foot': 0x13,
    'g_L_Hand': 0x14,
    'g_R_Foot': 0x15,
    'g_R_Hand': 0x16,
    'g_x_CAM': 0x17,
    'g_x_LND': 0x18,
}


class Page(ScrolledPanel):
    def __init__(self, parent, rows=32):
        ScrolledPanel.__init__(self, parent)
        self.sizer = wx.FlexGridSizer(rows=rows, cols=2, hgap=10, vgap=10)
        self.SetSizer(self.sizer)
        self.SetupScrolling()


class BasePanel(wx.Panel):
    def __init__(self, parent, root, name, item_type):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        self.root = root
        self.item = None
        self.entry = None
        self.saved_values = {}
        self.item_type = item_type
        self.edit_thread = None

        self.notebook = wx.Notebook(self)
        self.entry_page = Page(self.notebook)
        self.unknown_page = Page(self.notebook)

        self.notebook.AddPage(self.entry_page, name)
        self.notebook.AddPage(self.unknown_page, 'Unknown')

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.notebook, 1, wx.ALL | wx.EXPAND, 10)

        self.start_time = self.add_num_entry(self.entry_page, 'Start Time')
        self.duration = self.add_num_entry(self.entry_page, 'Duration')
        self.u_04 = self.add_hex_entry(self.unknown_page, 'U_04', max=0xFFFF)
        self.character_type = self.add_single_selection_entry(
            self.entry_page, 'Character Type', -1, choices={
                'Both': 0x0,
                'CAC Only': 0x01,
                'Roster Only': 0x02,
                'Legacy': 0x05
            })
        # self.Bind(wx.EVT_SET_FOCUS, self.on_focus)
        self.Bind(wx.EVT_TEXT, self.on_edit)
        self.Bind(wx.EVT_CHECKBOX, self.save_entry)
        self.Bind(wx.EVT_RADIOBOX, self.save_entry)
        self.Bind(wx.EVT_COLOURPICKER_CHANGED, self.save_entry)
        EVT_RESULT(self, self.save_entry)

        pub.subscribe(self.focus_on, 'focus_on')

        self.SetSizer(sizer)
        self.SetAutoLayout(1)

    def __getitem__(self, item):
        return self.__getattribute__(item)

    @add_entry
    def add_hex_entry(self, panel, _, *args, **kwargs):
        return HexCtrl(panel, *args, **kwargs)

    @add_entry
    def add_text_entry(self, panel, _, *args, **kwargs):
        if 'size' not in kwargs:
            kwargs['size'] = (150, -1)
        return TextCtrl(panel, *args, **kwargs)

    @add_entry
    def add_num_entry(self, panel, _, *args, **kwargs):
        if 'size' not in kwargs:
            kwargs['size'] = (150, -1)
        kwargs['min'], kwargs['max'] = 0, 65535
        return wx.SpinCtrl(panel, *args, **kwargs)

    @add_entry
    def add_unknown_num_entry(self, panel, _, *args, **kwargs):
        if 'size' not in kwargs:
            kwargs['size'] = (150, -1)
        kwargs['min'], kwargs['max'] = 0, 65535
        return NumCtrl(panel, *args, **kwargs)

    @add_entry
    def add_single_selection_entry(self, panel, _, *args, **kwargs):
        return SingleSelectionBox(panel, *args, **kwargs)

    @add_entry
    def add_multiple_selection_entry(self, panel, _, *args, **kwargs):
        return MultipleSelectionBox(panel, *args, **kwargs)

    @add_entry
    def add_unknown_hex_entry(self, panel, _, *args, **kwargs):
        if 'size' not in kwargs:
            kwargs['size'] = (150, -1)
        return UnknownHexCtrl(panel, *args, **kwargs)

    @add_entry
    def add_float_entry(self, panel, _, *args, **kwargs):
        if 'size' not in kwargs:
            kwargs['size'] = (150, -1)
        if 'min' not in kwargs:
            kwargs['min'] = -3.402823466e38
        if 'max' not in kwargs:
            kwargs['max'] = 3.402823466e38

        return wx.SpinCtrlDouble(panel, *args, **kwargs)

    @add_entry
    def add_color_picker(self, panel, _, *args, **kwargs):
        return ColourPickerCtrl(panel, *args, **kwargs)

    def add_nameable_float_entry(self, panel, *args, **kwargs):
        label = wx.StaticText(panel, -1, '')
        panel.sizer.Add(label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        control = self.add_float_entry(panel, None, *args, **kwargs)
        return label, control

    def on_edit(self, _):
        if not self.edit_thread:
            self.edit_thread = EditThread(self)
        else:
            self.edit_thread.new_sig()

    def hide_entry(self, name):
        try:
            label = self.__getattribute__(name + '_label')
            label.SetLabelText('')
        except AttributeError:
            pass
        control = self.__getattribute__(name)
        if control.IsEnabled():
            control.Disable()
            self.saved_values[name] = control.GetValue()
            control.SetValue(0.0)

    def show_entry(self, name, text, default=None):
        try:
            label = self.__getattribute__(name + '_label')
            label.SetLabelText(text)
        except AttributeError:
            pass
        control = self.__getattribute__(name)
        if not control.IsEnabled():
            control.Enable()
            #UNLEASHED: what is this? commented out because it because
            #the previous value gets saved as 0 after the control gets disabled
            #and renabing it restores that saved value (which is 0)
            #even though the actual value might not be 0
            #we are gonna read the data from the entry anyway, so i don't understand the saved value thing
            #control.SetValue(self.saved_values.get(name, default))

    def load_entry(self, item, entry):
        self.item = item
        self.saved_values = {}
        for name in entry.__fields__:
            self[name].SetValue(entry[name])
        self.entry = entry

    def save_entry(self, _):
        self.edit_thread = None
        if self.entry is None:
            return
        start_time_tmp = self.entry.start_time

        #create the backup tmp's, but make sure its the correct type so no NULL val is returned
        #is this needed? is there an easier way  to write this?
        if self.entry.bac_record.__name__ == "BACAnimation":
            ean_type_tmp = self.entry.ean_type
        elif self.entry.bac_record.__name__ == "BACHitbox":
            bdm_type_tmp = self.entry.bdm_type
        elif self.entry.bac_record.__name__ == "BACEffect":
            eepk_type_tmp = self.entry.eepk_type
        elif self.entry.bac_record.__name__ == "BACCamera":
            ean_type_tmp = self.entry.ean_type
        elif self.entry.bac_record.__name__ == "BACSound":
            acb_type_tmp = self.entry.acb_type
        elif self.entry.bac_record.__name__ == "BACProjectile":
            skill_type_tmp = self.entry.skill_type
        elif self.entry.bac_record.__name__ == "BACSystem":
            function_type_tmp = self.entry.function_type
        elif self.entry.bac_record.__name__ == "BACTargetingAssistance":
            rotation_axis_tmp = self.entry.rotation_axis
        elif self.entry.bac_record.__name__ == "BACEyeMovement":
            direction_type_tmp = self.entry.direction_type
        elif self.entry.bac_record.__name__ == "BACAuraEffect":
            aura_type_tmp = self.entry.aura_type
        elif self.entry.bac_record.__name__ == "BACPhysics":
            function_type_tmp = self.entry.function_type
        elif self.entry.bac_record.__name__ == "BACPartInvisibility":
            bcs_part_id_tmp = self.entry.bcs_part_id
        elif self.entry.bac_record.__name__ == "BACScreenEffect":
            bpe_effect_id_tmp = self.entry.bpe_effect_id


        do_update_startime = False
        do_update_maintype = False

        for name in self.entry.__fields__:
            control = self[name]
            # SpinCtrlDoubles suck
            if isinstance(control, wx.SpinCtrlDouble):
                try:
                    self.entry[name] = float(control.Children[0].GetValue())
                except ValueError:
                    # Keep old value if its mistyped
                    pass
            else:
                self.entry[name] = control.GetValue()

        if self.entry.start_time != start_time_tmp:
            do_update_startime = True


        ##UNLEASHED: check exclusive type updates
        if self.entry.bac_record.__name__ == "BACAnimation":
            do_update_maintype = True if self.entry.ean_type != ean_type_tmp else False
        elif self.entry.bac_record.__name__ == "BACHitbox":
            do_update_maintype = True if self.entry.bdm_type != bdm_type_tmp else False
        elif self.entry.bac_record.__name__ == "BACEffect":
            do_update_maintype = True if self.entry.eepk_type != eepk_type_tmp else False
        elif self.entry.bac_record.__name__ == "BACCamera":
            do_update_maintype = True if self.entry.ean_type != ean_type_tmp else False
        elif self.entry.bac_record.__name__ == "BACSound":
            do_update_maintype = True if self.entry.acb_type != acb_type_tmp else False
        elif self.entry.bac_record.__name__ == "BACProjectile":
            do_update_maintype = True if self.entry.skill_type != skill_type_tmp else False
        elif self.entry.bac_record.__name__ == "BACSystem":
            do_update_maintype = True if self.entry.function_type != function_type_tmp else False
        elif self.entry.bac_record.__name__ == "BACTargetingAssistance":
            do_update_maintype = True if self.entry.rotation_axis != rotation_axis_tmp else False
        elif self.entry.bac_record.__name__ == "BACEyeMovement":
            do_update_maintype = True if self.entry.direction_type != direction_type_tmp else False
        elif self.entry.bac_record.__name__ == "BACAuraEffect":
            do_update_maintype = True if self.entry.aura_type != aura_type_tmp else False
        elif self.entry.bac_record.__name__ == "BACPhysics":
            do_update_maintype = True if self.entry.function_type != function_type_tmp else False
        elif self.entry.bac_record.__name__ == "BACPartInvisibility":
            do_update_maintype = True if self.entry.bcs_part_id != bcs_part_id_tmp else False
        elif self.entry.bac_record.__name__ == "BACScreenEffect":
            do_update_maintype = True if self.entry.bpe_effect_id != bpe_effect_id_tmp else False


        if do_update_startime:
            pub.sendMessage('update_item', item=self.item, entry=self.entry)
            pub.sendMessage('reindex')
        if do_update_maintype:
            pub.sendMessage('reindex')








    def focus_on(self, entry):
        if not self.IsShown():
            return
        page = self.notebook.FindPage(self[entry].GetParent())
        self[entry].SetFocus()
        self.notebook.ChangeSelection(page)

    def on_focus(self, e):
        pub.sendMessage('set_focus', focus=e.GetWindow())

