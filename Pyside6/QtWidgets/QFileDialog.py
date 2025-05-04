# coding:utf-8
import random
import re
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction, QIcon, QDesktopServices
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar, QSize, QUrl, QRect
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar, QToolButton, QStatusBar, QMainWindow, QDockWidget, QDialog, QMdiArea, QMdiSubWindow, QFontDialog, \
    QColorDialog, QFileDialog

from Interface import WidgetInterface


class QFileDialogInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.infos.deleteLater()

        self.dialog = QFileDialog(self)
        self.box.addWidget(self.button)
        self.button.clicked.connect(self.dialog.show)

        # 设置默认的拓展名
        # self.dialog.setDefaultSuffix()

        self.dialog.getExistingDirectory()
        self.dialog.getExistingDirectoryUrl()

        self.dialog.getOpenFileName()
        self.dialog.getOpenFileNames()

        self.dialog.getOpenFileUrl()
        self.dialog.getOpenFileUrls()

        self.dialog.getSaveFileName()
        self.dialog.getSaveFileUrl()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QFileDialogInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
