# coding:utf-8

import sys

from PySide6.QtGui import QFont, Qt, QTextCharFormat, QTextDocument, QColor, QTextImageFormat, QIcon, QAction
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QScrollArea, QVBoxLayout, QLabel, QLineEdit, \
    QPushButton, QComboBox, QScrollBar, QSlider, QDial, QMenu, QCheckBox, QCalendarWidget

from PySide6.QtCore import QCalendar

from Interface import WidgetInterface


class QCalendarInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        calendar = QCalendar()

        # 获取年月日是否有效
        print(calendar.isDateValid(1145, 1, 1))
        print(calendar.isDateValid(2022, 2, 111))

        # 返回指定年月日构成的日期
        print(calendar.dateFromParts(2025, 4, 21))

        # 获取指定年指定月的总天数
        print(calendar.daysInMonth(2, 2022))

        # 获取指定年的总天数
        print(calendar.daysInYear(2024))

        # 获取是否为闰年
        print(calendar.isLeapYear(2024))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QCalendarInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())