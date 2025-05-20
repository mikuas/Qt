# coding:utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTreeView, QHBoxLayout
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

class StandarItem(QStandardItem):
    
    # 添加行, 列
    def appendColumn(self, items): ...
    def appendRows(self, items): ...
    
    # 获取父项数据
    def parent(self): ...
    
    pass

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.box = QHBoxLayout(self)
        self.standardItemModel = QStandardItemModel(self)
        # 设置表头
        self.standardItemModel.setHorizontalHeaderLabels(["列1", "列2", "列3"])
        # self.standardItemModel.setHeaderData()
        
        # 移除水平,垂直表头项
        # self.standardItemModel.takeHorizontalHeaderItem(0)
        # self.standardItemModel.takeVerticalHeaderItem(0)
        
        # 获取根目录的项
        print(self.standardItemModel.invisibleRootItem())
        
        # 清除所有数据项, 清除项中的数据
        # self.standardItemModel.clear()
        # self.standardItemModel.clearItemData()
        
        # 获取是否有子项
        print(self.standardItemModel.hasChildren())
        
        # 设置排序
        self.standardItemModel.setSortRole(Qt.DisplayRole)
        
        # self.standardItemModel.setRowCount(10)
        
        self.standardItemModel.appendRow(QStandardItem("Hello World"))
        self.standardItemModel.setItem(1, 1, QStandardItem("Hello StandardItemModel"))
        
        self.standardItemModel.item(0, 0).appendRow(QStandardItem("Hello StandarItemModel"))
        
        self.standardItemModel.item(0, 0).child(0, 0).appendRow(QStandardItem("Hello Qt"))
        
        self.treeView = QTreeView(self)
        self.treeView.setModel(self.standardItemModel)
        self.box.addWidget(self.treeView)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())