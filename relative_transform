from PySide2 import QtCore as qc
from PySide2 import QtWidgets as qg
import maya.OpenMayaUI as omui
import maya.cmds as cmds
import shiboken2

def get_maya_window():
    ptr = omui.MQtUtil.mainWindow()
    if ptr is not None:
        return shiboken2.wrapInstance(int(ptr), qg.QWidget)

class SetPosition(qg.QWidget):
    def __init__(self, parent=None):
        super(SetPosition, self).__init__(parent)
        
        self.setWindowTitle("Set Position")
        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint | qc.Qt.FramelessWindowHint)
        self.setWindowOpacity(0.75)
        self.setFixedWidth(150)
        self.setFixedHeight(40)
        self.keyPressEvent = self.KeyPress
        
        layout = qg.QGridLayout(self)
        
        self.entry_x = qg.QLineEdit()
        layout.addWidget(self.entry_x, 1, 1)
        
        self.entry_y = qg.QLineEdit()
        layout.addWidget(self.entry_y, 1, 2)
        
        self.entry_z = qg.QLineEdit()
        layout.addWidget(self.entry_z, 1, 3)

        # Timer for checking if no input is active
        self.timer = qc.QTimer(self)
        self.timer.timeout.connect(self.check_inputs)
        self.timer.start(1)  # Check every second

    def KeyPress(self, event):
        if event.key() in (qc.Qt.Key_Return, qc.Qt.Key_Enter):
            cmds.move(self.entry_x.text() if self.entry_x.text() else 0,
                      self.entry_y.text() if self.entry_y.text() else 0,
                      self.entry_z.text() if self.entry_z.text() else 0,
                      relative=True)
            self.hide()
        elif event.key() == qc.Qt.Key_Escape:
            self.hide()

    def eventFilter(self, obj, event):
        if event.type() == qc.QEvent.MouseButtonPress:
            global_pos = event.globalPos()
            if not self.geometry().contains(global_pos):
                self.hide()
                return True
        return super(SetPosition, self).eventFilter(obj, event)

    def check_inputs(self):
        # Check if none of the inputs have focus
        if not self.entry_x.hasFocus() and not self.entry_y.hasFocus() and not self.entry_z.hasFocus():
            self.hide()

# Create an instance of the widget
widget = SetPosition(get_maya_window())

# Install the event filter on the widget itself
widget.installEventFilter(widget)

# Show the widget
widget.show()

# Set focus to the first input field after showing the widget
widget.entry_x.setFocus()

# Center the widget in the Maya window
maya_window = get_maya_window()
widget.move(maya_window.frameGeometry().center() - widget.rect().center())
