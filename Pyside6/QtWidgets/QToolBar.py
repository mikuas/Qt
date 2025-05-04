# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar

from Interface import WidgetInterface

exec('''
print("Hello World")
print([_ for _ in range(100)])
''')


class QToolBarInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.toolBar = QToolBar("ToolBar", self)
        self.toolBar.addWidget(QLineEdit())

        self.box.addWidget(self.toolBar)
        self.toolBar.addAction(QAction("Action", self))
        self.toolBar.addWidget(QLineEdit())

        # 设置工具栏方向
        self.toolBar.setOrientation(Qt.Orientation.Vertical)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QToolBarInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
