# coding:utf-8
import random
import re
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction, QIcon, QDesktopServices
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar, QToolButton, QStatusBar, QMainWindow, QDockWidget, QDialog, QMdiArea, QMdiSubWindow
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar, QSize, QUrl


from Interface import WidgetInterface


class QMdiArea_QMdiSubWindow_Interface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.mdiArea = QMdiArea(self)
        self.mdiSubWindow = QMdiSubWindow(self)

        self.box.addWidget(self.mdiArea)
        self.box.addWidget(self.mdiSubWindow)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMdiArea_QMdiSubWindow_Interface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
