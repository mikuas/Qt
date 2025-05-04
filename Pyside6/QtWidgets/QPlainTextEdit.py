# coding:utf-8

import sys

from PySide6.QtCore import QPoint
from PySide6.QtGui import QFont, Qt, QTextCharFormat, QTextDocument, QColor, QTextImageFormat
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QScrollArea, QVBoxLayout, QLabel, QLineEdit, QPushButton, QPlainTextEdit

from Interface import WidgetInterface


class QPlantEditInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.plainEdit = QPlainTextEdit(self)
        self.plainEdit.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.box.addWidget(self.plainEdit)
        self.box.addWidget(self.button)
        self.box.addWidget(self.infos)

    # def mouseReleaseEvent(self, event):
    #     if event.button() == Qt.MouseButton.RightButton:
    #         self.plainEdit.customContextMenuRequested.emit(QPoint(event.x(), event.y()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QPlantEditInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
    ...