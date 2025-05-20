# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QToolBox
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar
from PySide6.QtWebEngineWidgets import QWebEngineView

from Interface import WidgetInterface


class QToolBoxInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.toolBox = QToolBox(self)
        self.box.addWidget(self.toolBox)

        self.toolBox.addItem(QLabel("Hello World"), "Hello")
        self.toolBox.addItem(QLabel("Ciallo World"), "Ciallo")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QToolBoxInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())

