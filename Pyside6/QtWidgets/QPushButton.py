# coding:utf-8

import sys

from PySide6.QtGui import QFont, Qt, QTextCharFormat, QTextDocument, QColor, QTextImageFormat, QIcon, QAction
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QScrollArea, QVBoxLayout, QLabel, QLineEdit, \
    QPushButton, QComboBox, QScrollBar, QSlider, QDial, QMenu

from Interface import WidgetInterface


class QPushButtonInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        button = QPushButton("Click Me")

        # 创建一个 QMenu
        menu = QMenu(self)

        # 创建一些 QAction，并将它们添加到菜单中
        action1 = QAction("Option 1", button)
        action2 = QAction("Option 2", button)
        action3 = QAction("Option 3", button)

        menu.addAction(action1)
        menu.addAction(action2)
        menu.addAction(action3)

        action1.setShortcut("Alt+1")
        action2.setShortcut("Alt+2")
        action3.setShortcut("Alt+3")

        # 设置按钮的菜单
        button.setMenu(menu)

        # 当选择菜单项时的行为
        def on_action_triggered():
            print("An option was selected!")

        action1.triggered.connect(on_action_triggered)
        action2.triggered.connect(on_action_triggered)
        action3.triggered.connect(on_action_triggered)

        self.box.addWidget(button)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QPushButtonInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
    ...