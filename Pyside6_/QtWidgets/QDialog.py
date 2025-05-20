# coding:utf-8
import random
import re
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction, QIcon, QDesktopServices
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar, QToolButton, QStatusBar, QMainWindow, QDockWidget, QDialog, QMdiArea, QMdiSubWindow
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar, QSize, QUrl, QRect

from Interface import WidgetInterface


class QDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        try:

            from qframelesswindow import WindowEffect, StandardTitleBar, FramelessWindow
            self.windowEffect = WindowEffect(self)
            self.windowEffect.setMicaEffect(self.winId(), isAlt=True)
            self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
            self.setWindowFlags(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.Dialog)
            self.titleBar = StandardTitleBar(self)
            self.titleBar.raise_()
            self.titleBar.minBtn.hide()
            self.titleBar.maxBtn.hide()
            self.titleBar.setDoubleClickEnabled(False)
            self.titleBar.setContentsMargins(0, 0, 6, 0)
        except ImportError:
            ...

    def resizeEvent(self, arg__1):
        super().resizeEvent(arg__1)
        try:
            self.titleBar.resize(self.width(), self.titleBar.height())
        except Exception:
            ...


class QDialogInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.infos.deleteLater()

        self.dialog = QDialog(self)

        self.button.clicked.connect(self.dialog.show)
        self.box.addWidget(self.button)

        # 设置对话框模式特性
        self.dialog.setWindowModality(Qt.WindowModality.NonModal)

        # 以模式方法显示对话框
        # self.dialog.open()

        # 以模式方式显示对话框, 返回对话框值
        # self.dialog.exec()

        # 设置对话框为模式对话框
        self.dialog.setModal(True)

        # 隐藏对话框
        # self.dialog.accept() 将返回值设置为QDialog.Accepted      发送 accepted | finished 信号
        # self.dialog.reject() 将返回值设置为int                   发送 finished 信号



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDialogInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
