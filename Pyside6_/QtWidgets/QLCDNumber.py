# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar

from Interface import WidgetInterface


class QLCDNumberInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.lcd = QLCDNumber(self)
        self.box.addWidget(self.lcd)

        # 设置可显示数字个数
        self.lcd.setDigitCount(10)

        # 设置外观样式
        # self.lcd.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        # 显示字符串
        self.lcd.display('Ciallo World')

        self.lcd.display(1145)

        self.lcd.display(100.12321)

        # 设置数字显示模式
        self.lcd.setMode(QLCDNumber.Mode.Dec)

        print(self.lcd.value())

        # 设置小数点的显示是否会占用一位
        self.lcd.setSmallDecimalPoint(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLCDNumberInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())