For older Maya versions you have to edit import of PySide and shiboken.
Example:

Maya 2025:
```
from PySide6 import QtCore as qc
from PySide6 import QtWidgets as qg
import maya.OpenMayaUI as omui
import maya.cmds as cmds
import shiboken6 as shiboken
```

Maya 2022:
```
from PySide2 import QtCore as qc
from PySide2 import QtWidgets as qg
import maya.OpenMayaUI as omui
import maya.cmds as cmds
import shiboken2 as shiboken
```



