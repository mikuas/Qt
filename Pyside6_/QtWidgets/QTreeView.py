# coding:utf-8

import sys
from PySide6.QtWidgets import QApplication, QWidget, QTreeView, QHBoxLayout, QHeaderView
from PySide6.QtCore import Qt, QStringListModel


class TreeView(QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.stringListModel = QStringListModel(self)
        self.stringListModel.setStringList([
            'Root Item'
        ])

        # 设置数据模型
        self.setModel(self.stringListModel)
        
        # 设置表头
        # self.setHeader(QHeaderView(Qt.Orientation.Horizontal, self))
        
        
        

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.box = QHBoxLayout(self)
        
        self.treeView = TreeView(self)
        self.box.addWidget(self.treeView)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())