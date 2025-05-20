import sys
from typing import List, Union

from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPalette, QCursor, QPixmap


class APP(QApplication):
    def __init__(self):
        super().__init__()
        # self.setAutoSipEnabled(True)
    
    # 设置应用程序当前光标
    def setOverrideCursor(self, arg__1: Union[QCursor, Qt.CursorShape, QPixmap]) -> object:
        super().setOverrideCursor(arg__1)
    
    # 设置程序中的布局方向
    def setLayoutDirection(self, direction: Qt.LayoutDirection) -> None:
        super().setLayoutDirection(direction)
    
    # 获取顶层窗口列表
    def topLevelWidgets(self) -> List[QWidget]:
        return super().topLevelWidgets()
    
    # 获取指定位置窗口
    def widgetAt(self, pos: QPoint) -> QWidget | None: # (x: int, y: int)
        return super().widgetAt(pos)
    
    # 获取指定位置的顶层窗口
    def topLevelAt(self, pos: QPoint) -> QWidget | None: # (x: int, y: int)
        return super().topLevelAt(pos)

    # 滚轮滚动时,界面控件移动的行数, 默认为3
    def setWheelScrollLines(self, line: int) -> None:
        super().setWheelScrollLines(line)
    
    # 设置程序默认调色板
    def setPalette(self, palette, className=None) -> None:
        super().setPalette(palette, className)
    
    # 获取程序默认调试板
    def palette(self) -> QPalette:
        return super().palette()

    # 设置界面特效
    def setEffectEnabled(self, arg__1: Qt.UIEffect, enable=True) -> None:
        super().setEffectEnabled(arg__1, enable)

    # 获取样式表
    def styleSheet(self) -> str:
        return super().styleSheet()
    
    # 当最后一个窗口关闭时, 程序是否退出, 默认为 True
    def setQuitOnLastWindowClosed(self, quit: bool) -> None:
        super().setQuitOnLastWindowClosed(quit)
        
    # 发出响铃
    def beep(self) -> None:
        super().beep()

    def exec(self) -> int:
        return super().exec()


class Window_1(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(800, 520)
        self.setWindowTitle("Window_1")
    

class Window_2(Window_1):
    def __init__(self, parent=None, app=None):
        super().__init__(parent)
        self.setWindowTitle("Window_2")
        self.box = QVBoxLayout(self)

        self.btn = QPushButton("beep", self)
        self.btn.clicked.connect(app.beep)

        self.box.addWidget(self.btn)
    
    def closeEvent(self, event):
        event.ignore()
        self.hide()

if __name__ == "__main__":
    app = APP()
    window_1 = Window_1()
    window_2 = Window_2(app=app)
    window_1.show()
    window_2.show()
    window_1.raise_()
    sys.exit(app.exec())
    pass