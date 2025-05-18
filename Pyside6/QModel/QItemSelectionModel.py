# coding:utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt, QItemSelectionModel, QItemSelection


class Window(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())