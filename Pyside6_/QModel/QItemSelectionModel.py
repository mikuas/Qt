# coding:utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTreeView, QTreeWidget, \
    QListView, QListWidget, QHBoxLayout, QTreeWidgetItem, QStyledItemDelegate
from PySide6.QtCore import Qt, QItemSelectionModel, QItemSelection
from PySide6.QtGui import QStandardItemModel, QStandardItem

            
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.box = QHBoxLayout(self)
        
        self.listWidget = QListWidget(self)
        self.selectionModel = QItemSelectionModel(self.listWidget.model())
        self.listWidget.setSelectionModel(self.selectionModel)
        self.treeWidget = QTreeWidget(self)
        
        self.listWidget.addItems([
            f"Item {i}" for i in range(1, 11)
        ])
        self.treeWidget.addTopLevelItems([
            QTreeWidgetItem([f"Tree Item {i}"]) for i in range(1, 11)
        ])
        
        self.box.addWidget(self.listWidget)
        self.box.addWidget(self.treeWidget)
        
        # 清空选择模型并发送 selectionChanged | currentChanged Signal
        self.selectionModel.clear()
        
        # 清空选择模型, 但不发送信号
        self.selectionModel.reset()
        
        # 获取是否有选择项
        print(self.selectionModel.hasSelection())
        
        self.selectionModel.currentChanged.connect(lambda i: {
            print(f"CurrentChange: {i}"),
            print(self.selectionModel.selection())
            })
    
        # 选择集
        self.selection = self.selectionModel.selection()
        
        # 添加从左上角到右下角位置处的所有项
        # self.selection.select()
        
        # 与其他选择集合并
        # self.selection.merge()
        
        # 获取选择集中的数据索引列表
        print(self.selection.indexes())
        
        # 获取指定的选项是否在选择集中
        # print(self.selection.contains())
        
        # 清空选择集
        self.selection.clear()
        
        # 获取选择集中元素的个数
        print(self.selection.count())
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())