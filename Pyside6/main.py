# coding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt

from FluentWidgets import SmoothSwitchNavWidget, HorizontalSeparator

from QtCore.QMargins import QMarginInterface
from QtCore.QRect import QRectInterface
from QtGui.QColor import QColorInterface
from QtGui.QFont import QFontInterface
from QtGui.QPalette import QPaletteInterface
from QtWidgets.Interface import WidgetInterface


class Window(SmoothSwitchNavWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.hp = HorizontalSeparator(self)
        self._widgetLayout.insertWidget(1, self.hp)
        
        self.QMARGIN_INTERFACE = QMarginInterface(self)
        self.QRECT_INTERFACE = QRectInterface(self)
        self.QCOLOR_INTERFACE = QColorInterface(self)
        self.QFONT_INTERFACE = QFontInterface(self)
        self.QPALETTE_INTERFACE = QPaletteInterface(self)
        
        self.initNavigation()
        
        self.setCurrentWidget("QMargin Interface")
        for w in self.navigationBar.getAllWidget().values():
            w.setFixedWidth(110)
        self.navigationBar.setContentsMargins(0, 0, 0, 0)
        self.setNavigationAlignment(Qt.AlignmentFlag.AlignCenter)
                
    def initNavigation(self):
        self.addSubInterface(
            "QMargin Interface",
            "QMargin Interface",
            self.QMARGIN_INTERFACE
        )
        self.addSubInterface(
            "QRect Interface",
            "QRect Interface",
            self.QRECT_INTERFACE
        )
        self.addSubInterface(
            "QColor Interface",
            "QColor Interface",
            self.QCOLOR_INTERFACE
        )
        self.addSubInterface(
            "QFont Interface",
            "QFont Interface",
            self.QFONT_INTERFACE
        )
        self.addSubInterface(
            "QPalette Interface",
            "QPalette Interface",
            self.QPALETTE_INTERFACE
        )
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())