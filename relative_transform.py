from PySide6 import QtCore as qc
from PySide6 import QtWidgets as qg
import maya.OpenMayaUI as omui
import maya.cmds as cmds
import shiboken6 as shiboken

cmds.setToolTo('Move')

def get_maya_window():
    ptr = omui.MQtUtil.mainWindow()
    if ptr is not None:
        return shiboken.wrapInstance(int(ptr), qg.QWidget)

class SetPosition(qg.QDialog):
    def __init__(self, parent=None):
        super(SetPosition, self).__init__(parent, qc.Qt.FramelessWindowHint)
        
        self.setWindowTitle("Set Position")
        self.setWindowOpacity(1)
        self.setFixedWidth(150)
        self.setFixedHeight(40)
        
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

    def keyPressEvent(self, event):
        if event.key() in (qc.Qt.Key_Return, qc.Qt.Key_Enter):
            pivot_orient = cmds.manipMoveContext('Move', query=True, translate=True)
            
            try:
                input_x = float(self.entry_x.text()) if self.entry_x.text() else 0.0
            except ValueError:
                input_x = 0.0
                
            try:
                input_y = float(self.entry_y.text()) if self.entry_y.text() else 0.0
            except ValueError:
                input_y = 0.0
                
            try:
                input_z = float(self.entry_z.text()) if self.entry_z.text() else 0.0
            except ValueError:
                input_z = 0.0
            
            translation_input = [input_x, input_y, input_z]
            
            result = [x + y for x, y in zip(pivot_orient, translation_input)]
            
            cmds.manipMoveContext('Move', edit=True, translate=[result[0], result[1], result[2]])
            
            self.hide()
        elif event.key() == qc.Qt.Key_Escape:
            self.hide()

    def mousePressEvent(self, event):
        if not self.rect().contains(event.pos()):
            self.hide()

    def check_inputs(self):
        if not self.entry_x.hasFocus() and not self.entry_y.hasFocus() and not self.entry_z.hasFocus():
            self.hide()

# Create an instance of the dialog
dialog = SetPosition(get_maya_window())

# Show the dialog
dialog.show()

# Set focus to the first input field after showing the dialog
dialog.entry_x.setFocus()

# Center the dialog in the Maya window
maya_window = get_maya_window()
dialog.move(maya_window.frameGeometry().center() - dialog.rect().center())
