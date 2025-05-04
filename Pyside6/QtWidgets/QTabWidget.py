# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar

from Interface import WidgetInterface


class QTabWidgetInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.tableWidget = QTabWidget(self)

        self.box.addWidget(self.tableWidget)
        self.tableWidget.setTabShape(QTabWidget.TabShape.Triangular)

        # 添加卡片
        # QWidget, QIcon, label

        self.tableWidget.addTab(QLabel("INTERFACE_1"), "Tab1")
        self.tableWidget.addTab(QLabel("INTERFACE_2"), "Tab2")
        self.tableWidget.addTab(QLabel("INTERFACE_3"), "Tab3")
        self.tableWidget.addTab(QLabel("INTERFACE_4"), "Tab4")
        self.tableWidget.addTab(QLabel("INTERFACE_5"), "Tab5")

        self.tableWidget.setMovable(True)

        # 清空所有卡片
        # self.tableWidget.clear()

        # 设置卡片是否是文档模式
        self.tableWidget.setDocumentMode(True)

        # 设置卡片标题是否为省略模式
        self.tableWidget.setElideMode(Qt.TextElideMode.ElideRight)

        # 设置卡片标题是否自动隐藏
        self.tableWidget.setTabBarAutoHide(True)

        # 设置标题栏位置
        self.tableWidget.setTabPosition(QTabWidget.TabPosition.North)

        # 设置卡片是否可以关闭
        self.tableWidget.setTabsClosable(True)
        self.tableWidget.tabCloseRequested.connect(lambda index: print(index))

        # 设置是否有滚动按钮
        self.tableWidget.setUsesScrollButtons(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QTabWidgetInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())

