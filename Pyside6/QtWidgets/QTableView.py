# coding:utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableView, QHBoxLayout, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QItemSelectionModel, Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.box = QHBoxLayout(self)
        self.standardModel = QStandardItemModel(self)
        self.standardModel.appendRow(QStandardItem("Hello World"))
        
        self.standardModel.setHorizontalHeaderLabels(["Item1"])
        
        self.tabView = QTableView(self)
        self.tabView.setModel(self.standardModel)
        
        # 设置是否显示线条
        self.tabView.setShowGrid(True)
        
        # 选择指定范围内的数据项
        self.tabView.setSelection(self.rect(), QItemSelectionModel.SelectionFlag.Rows)
        
        self.tabView.resizeRowToContents(0)
        self.tabView.resizeColumnToContents(0)
        self.tabView.resizeColumnsToContents()
        self.tabView.resizeRowsToContents()
        
        self.tabView.setCornerButtonEnabled(True)
        # self.tabView.setHorizontalHeader(QHeaderView(Qt.Orientation.Horizontal, self))
        
        self.box.addWidget(self.tabView)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())