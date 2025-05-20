# coding:utf-8

import sys

from PySide6.QtGui import QFont, Qt, QTextCharFormat, QTextDocument, QColor, QTextImageFormat, QIcon, QAction
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QScrollArea, QVBoxLayout, QLabel, QLineEdit, \
    QPushButton, QComboBox, QScrollBar, QSlider, QDial, QMenu, QCheckBox, QRadioButton

from Interface import WidgetInterface


class QRadioButtonInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        button = QRadioButton("Click Me", self)

        self.box.addWidget(button)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QRadioButtonInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
    ...