# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar

from Interface import WidgetInterface


class QActionInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.action = QAction("Action_1", self)

        # 设置名称
        self.action.setText("Action_1")

        # 设置图标
        # self.action.setIcon()

        # 设置是否可以勾选
        self.action.setCheckable(True)

        # 设置菜单中图标是否可见
        self.action.setIconVisibleInMenu(True)

        # 将动作添加到菜单中
        # self.action.setMenu()

        # 设置快捷键
        # self.action.setShortcut()

        # 获取是否处于激活状态
        print(self.isEnabled())

        # 设置长按快捷键时是否可以重复执行动作,默认True
        self.action.setAutoRepeat(True)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QActionInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
