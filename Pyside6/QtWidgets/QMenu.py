# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar

from Interface import WidgetInterface


class QMenuInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.menu = QMenu("Menu", self)

        self.menu.addAction(QAction("Action_1", self))

        self.box.addWidget(self.menu)
        self.menu.setTearOffEnabled(True)

        # 插入子菜单
        # self.menu.insertMenu()

        # 从菜单中移除动作
        # self.menu.removeAction()

        # 获取菜单中的动作
        print(self.menu.actions())

        # 获取菜单对应动作
        print(self.menu.menuAction())


    def contextMenuEvent(self, event):
        super().contextMenuEvent(event)
        self.menu.exec(event.globalPos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMenuInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
