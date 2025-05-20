# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QToolBox
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar
from PySide6.QtWebEngineWidgets import QWebEngineView


class QWebEngineViewInterface(QWebEngineView):
    def __init__(self):
        super().__init__()

        # 加载网页
        self.load("https://www.baidu.com")

        # 重新加载网页
        self.reload()

        # 向前浏览网页
        self.forward()

        # 向后浏览网页
        self.back()

        # 获取当前网页的url
        print(self.url())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWebEngineViewInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())

