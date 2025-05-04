# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar

from Interface import WidgetInterface


class QWidgetActionInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.widgetAction = QWidgetAction(self)
        self.widgetAction.setDefaultWidget(QLineEdit())

        self.menu = QMenu(self)
        self.menu.addAction(self.widgetAction)

    def contextMenuEvent(self, event):
        super().contextMenuEvent(event)
        self.menu.exec(event.globalPos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidgetActionInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
