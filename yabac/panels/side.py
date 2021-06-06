import re
import sys

from pubsub import pub
import wx


from pyxenoverse.bac.sub_entry import ITEM_TYPES

from yabac.panels.types.entry_panel import EntryPanel
from yabac.panels.types.animation_panel import AnimationPanel
from yabac.panels.types.hitbox_panel import HitboxPanel
from yabac.panels.types.movement_panel import MovementPanel
from yabac.panels.types.invulnerability_panel import InvulnerabilityPanel
from yabac.panels.types.time_scale_panel import TimeScalePanel
from yabac.panels.types.tracking import TrackingPanel
from yabac.panels.types.chain_attack_parameters_panel import ChainAttackParametersPanel
from yabac.panels.types.bcm_callback_panel import BcmCallbackPanel
from yabac.panels.types.effect_panel import EffectPanel
from yabac.panels.types.projectile_panel import ProjectilePanel
from yabac.panels.types.camera_panel import CameraPanel
from yabac.panels.types.sound_panel import SoundPanel
from yabac.panels.types.targeting_assistance_panel import TargetingAssistancePanel
from yabac.panels.types.part_invisibility_panel import PartInvisibilityPanel
from yabac.panels.types.animation_modification_panel import AnimationModificationPanel
from yabac.panels.types.function_control_panel import FunctionControlPanel
from yabac.panels.types.screen_effect_panel import ScreenEffectPanel
from yabac.panels.types.throw_handler_panel import ThrowHandlerPanel
from yabac.panels.types.physics_panel import PhysicsPanel
from yabac.panels.types.aura_effect_panel import AuraEffectPanel
from yabac.panels.types.homing_movement_panel import HomingMovementPanel
from yabac.panels.types.eye_movement_panel import EyeMovementPanel
from yabac.panels.types.type22_panel import Type22Panel
from yabac.panels.types.transparency_effect_panel import TransparencyEffectPanel
from yabac.panels.types.dual_skill_data_panel import DualSkillDataPanel
from yabac.panels.types.charge_attack_parameters_panel import ChargeAttackParametersPanel
from yabac.panels.types.extended_camera_control_panel import ExtendedCameraControlPanel
from yabac.panels.types.effect_property_control_panel import EffectPropertyControlPanel

RE_PATTERN = re.compile(r".*'(.*[.])*(.*)'.*")


class SidePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        sizer = wx.BoxSizer()
        self.root = parent
        self.panels = {}
        self.current_panel = None
        entry_panel = EntryPanel(self)
        entry_panel.Hide()
        sizer.Add(entry_panel, 1, wx.ALL | wx.EXPAND, 10)
        self.panels = {'Entry': entry_panel}
        for bac_type in ITEM_TYPES.values():
            name = re.match(RE_PATTERN, str(bac_type)).group(2)
            panel_class = getattr(sys.modules[__name__], name + 'Panel')

            panel = panel_class(self, self.root, name, bac_type)
            panel.Hide()
            self.panels[name] = panel
            sizer.Add(panel, 1, wx.ALL | wx.EXPAND, 10)

        pub.subscribe(self.load_entry, 'load_entry')
        pub.subscribe(self.hide_panels, 'hide_panels')

        self.SetSizer(sizer)
        self.SetAutoLayout(1)

    def show_panel(self, panel, item, entry):
        if self.current_panel != panel:
            if self.current_panel:
                self.current_panel.Hide()
            self.current_panel = panel
            self.current_panel.Show()
            self.current_panel.Layout()
            self.Layout()
        self.current_panel.load_entry(item, entry)

    def hide_panels(self):
        for panel in self.panels.values():
            panel.Hide()
        pub.sendMessage('clear_focus')
        self.current_panel = None
        self.Layout()

    def load_entry(self, item, entry):
        entry_type = type(entry)
        if entry_type.__name__ == 'Entry' or entry_type in ITEM_TYPES.values():
            name = entry_type.__name__
            self.show_panel(self.panels[name], item, entry)
        else:
            self.hide_panels()


