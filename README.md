For older Maya verions you have to edit import of PySide and shiboken from 6 to 2.
Example:

2025:
```
from PySide6 import QtCore as qc
from PySide6 import QtWidgets as qg
import maya.OpenMayaUI as omui
import maya.cmds as cmds
import shiboken6 as shiboken
```

2022:
```
from PySide2 import QtCore as qc
from PySide2 import QtWidgets as qg
import maya.OpenMayaUI as omui
import maya.cmds as cmds
import shiboken2 as shiboken
```



