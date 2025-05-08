# coding:utf-8
from FluentWidgets import FluentWindow
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QLabel, QPushButton, QTabWidget, QTabBar, QApplication
)
from PySide6.QtCore import Qt
import sys


class Window(FluentWindow):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.resize(600, 400)
    win.show()
    sys.exit(app.exec())
