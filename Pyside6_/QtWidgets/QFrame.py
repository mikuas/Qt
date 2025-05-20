# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar

from Interface import WidgetInterface


class QFrameInterface(QFrame):
    def __init__(self):
        super().__init__()

        # 设置QFrame窗口的阴影形式
        self.setFrameShadow(QFrame.Shadow.Raised)

        # 设置边框形状
        self.setFrameShape(QFrame.Shape.StyledPanel)
        # 绘制边框线
        # self.drawFrame()

        # 设置布局
        # self.setLayout()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QFrameInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())