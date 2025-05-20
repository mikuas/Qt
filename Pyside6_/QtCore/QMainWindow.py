# coding:utf-8
import random
import re
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction, QIcon, QDesktopServices
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar, QToolButton, QStatusBar, QMainWindow
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar, QSize, QUrl


class QMainWindowInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.box = QVBoxLayout()
        for _ in range(5):
            self.menuBar().addAction(QAction(f"Action_{str(_)}", self))
        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.box)

        self.label = QLabel("Hello World")
        palette = self.label.palette()
        palette.setColor(QPalette.ColorRole.WindowText, QColor("deeppink"))
        self.label.setPalette(palette)
        self.label.setFont(QFont(self.label.font().family(), 32))

        self.title = QLabel("Title")
        self.title.setFont(QFont(self.title.font().family(), 64))

        self.box.addWidget(self.title, 1, Qt.AlignmentFlag.AlignHCenter)
        self.box.addWidget(self.label, 1, Qt.AlignmentFlag.AlignHCenter)

        self.statusBar().addWidget(QLabel("Status Bar", self))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindowInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
