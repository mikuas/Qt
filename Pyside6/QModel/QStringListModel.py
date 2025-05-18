# coding:utf-8

import sys
from PySide6.QtWidgets import QApplication, QWidget, QListView
from PySide6.QtCore import Qt, QStringListModel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.stringListModel = QStringListModel(self)
        
        self.stringListModel.setStringList([
            'Hello World',
            'Hello Qt',
            'Hello PySide6',
            'Hello Python'
        ])
        
        print(self.stringListModel.stringList())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())