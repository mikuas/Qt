# coding:utf-8
import random
import re
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction, QIcon, QDesktopServices
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar, QToolButton, QStatusBar, QMainWindow, QDockWidget, QDialog
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar, QSize, QUrl


from Interface import WidgetInterface


class QDockWidgetInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.infos.deleteLater()

        self.dockWidget = QDockWidget("DockWidget", self)
        # 设置可停靠区域
        self.dockWidget.setAllowedAreas(Qt.DockWidgetArea.TopDockWidgetArea)

        # self.box.addWidget()

        self.dialog = QDialog(self)
        self.dialog.setFixedSize(500, 320)
        try:
            from FluentWidgets import MessageDialog, Dialog
            from qframelesswindow import WindowEffect
            self.wef = WindowEffect(self.dialog)
            self.wef.setMicaEffect(self.dialog.winId(), isAlt=True)
            self.dialog.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        except ImportError: ...

        self.dialog.setWindowFlags(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.Dialog)

        # 设置成浮动状态
        # self.dockWidget.setFloating(True)

        self.box.addWidget(self.button)
        self.button.clicked.connect(self.dialog.show)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDockWidgetInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
