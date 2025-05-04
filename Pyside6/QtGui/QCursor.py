import sys

from typing import overload

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget, QTextBrowser, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QComboBox
from PySide6.QtGui import QPalette, QColor, QCursor, Qt, QPixmap

# from Interface import WidgetInterface
from .Interface import WidgetInterface


class QCursorInterface(WidgetInterface):
    def __init__(self, parent=None):
        super().__init__(parent, True)
        self.edit.setPlaceholderText("指针路径")
        self.button.setText("Apply")
        self.button.clicked.connect(self.updateCursor)
        
        self.p = QPixmap()

        self.cursor = QCursor()
        self.cursor.setShape(Qt.CursorShape.ForbiddenCursor)
        
        self.setCursor(self.cursor)
        
        self.box.addWidget(self.edit)
        self.box.addWidget(self.button)
        self.box.addWidget(self.infos)
        
    def updateCursor(self):
        self.infos.append(f"已加载鼠标样式,路径: {self.edit.text()}" if self.p.load(self.edit.text()) else "加载失败")
        self.cursor = QCursor(self.p)
        self.setCursor(self.cursor)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QCursorInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())