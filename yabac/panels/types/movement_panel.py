import wx
from yabac.panels.types import BasePanel, Page


class MovementPanel(BasePanel):
    def __init__(self, *args):
        BasePanel.__init__(self, *args)
        matrix_page = Page(self.notebook)
        self.notebook.InsertPage(1, matrix_page, 'Matrix')

        self.movement_flags = self.add_multiple_selection_entry(
            self.entry_page, 'Movement Flags', orient=wx.VERTICAL, cols=4, choices=[
                ('', [None, None, None, 'Orientation Follows Direction'], True),
                ('', ['Allow Teleport', None, 'Up', 'Down'], True),
                ('', [None, None, None, 'No Orientation'], True),
                ('', ['Automatic in direction', 'Automatic towards opponent', 'Manual', 'Teleport to opponent'], True)
            ])
        self.u_0a = self.add_hex_entry(self.unknown_page, 'U_0A')
        self.x_axis_movement = self.add_float_entry(matrix_page, 'X Axis Movement')
        self.y_axis_movement = self.add_float_entry(matrix_page, 'Y Axis Movement')
        self.z_axis_movement = self.add_float_entry(matrix_page, 'Z Axis Movement')
        self.x_axis_drag = self.add_float_entry(matrix_page, 'X Axis Drag')
        self.y_axis_drag = self.add_float_entry(matrix_page, 'Y Axis Drag')
        self.z_axis_drag = self.add_float_entry(matrix_page, 'Z Axis Drag')

