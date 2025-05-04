# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar

from Interface import WidgetInterface


class QMenuBarInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.menuBar = QMenuBar(self)

        self.menuBar.addAction(QAction("File", self))
        self.menuBar.addAction(QAction("Edit", self))
        self.menuBar.addAction(QAction("View", self))

        self.menu = QMenu("Menu", self)
        self.menu.addAction(QAction("Menu1", self))
        # 添加分隔符
        self.menu.addSeparator()
        self.menu.addAction(QAction("Menu2", self))
        self.menuBar.addMenu(self.menu)

        # 设置高亮显示的动作
        action = QAction("Action", self)
        self.menuBar.addAction(action)
        self.menuBar.setActiveAction(action)

        # 在菜单栏角落位置添加控件
        self.menuBar.setCornerWidget(QLabel("Corner Widget"), Qt.Corner.BottomRightCorner)

        self.box.addWidget(self.menuBar, alignment=Qt.AlignmentFlag.AlignTop)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMenuBarInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
