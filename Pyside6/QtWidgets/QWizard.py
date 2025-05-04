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
    QColorDialog, QFileDialog, QInputDialog, QMessageBox, QErrorMessage, QProgressDialog, QWizard, QWizardPage, QStyle

from Interface import WidgetInterface


class QWizardInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.infos.deleteLater()

        self.wizard = QWizard(self)
        self.box.addWidget(self.button)
        self.button.clicked.connect(self.wizard.show)

        # 添加向导页,并返回ID号
        page = QWizardPage()
        self.wizard.addPage(page)

        self.wizard.setWindowTitle("QWizard")

        # 用指定的ID号添加向导
        # self.wizard.setPage(1, page)

        # 移除向导项
        # self.wizard.removePage()

        # 获取当前向导页
        print(self.wizard.currentPage())

        # 获取向导页是否被访问过
        # self.wizard.hasVisitedPage()

        # 回到初始页
        self.wizard.restart()

        # 显示上一页
        self.wizard.back()

        # 显示下一页
        self.wizard.next()

        # 获取置顶ID号的向导页
        # self.wizard.page()

        # 获取向导页的ID列表
        print(self.wizard.pageIds())

        # 获取下一页的ID号
        print(self.wizard.nextId())


        self.wizard.setWizardStyle(QWizard.WizardStyle.AeroStyle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWizardInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
