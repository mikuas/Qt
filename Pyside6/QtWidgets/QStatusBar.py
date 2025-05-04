# coding:utf-8
import random
import re
import sys

from FluentWidgets import themeColor
from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction, QIcon, QDesktopServices
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar, QToolButton, QStatusBar
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar, QSize, QUrl

from Interface import WidgetInterface


class QStatusBarInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.statusBar = QStatusBar(self)
        self.statusBar.setFont(QFont("微软雅黑", 32))
        self.box.addWidget(self.statusBar, alignment=Qt.AlignmentFlag.AlignBottom)

        # 显示信息, timeout是显示时间
        self.statusBar.showMessage("Ciallo World", 5000)
        # 获取当前显示的信息
        print(self.statusBar.currentMessage())
        # 删除信息
        self.statusBar.clearMessage()

        # 在状态栏右边添加永久控件
        self.statusBar.addPermanentWidget(QLabel("Ciallo World"))
        # 设置右下角是否有三角形
        self.statusBar.setSizeGripEnabled(False)
        # 确保右边的控件可见
        self.statusBar.hideOrShow()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QStatusBarInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
