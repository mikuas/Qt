# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar

from Interface import WidgetInterface


class QDateTimeEditInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.dtEdit = QDateTimeEdit(self)
        self.box.addWidget(self.dtEdit)

        # 设置时间
        self.dtEdit.setTime(QTime().currentTime())

        # 设置日期
        self.dtEdit.setDate(QDate().currentDate())

        # 设置是否有日历控件
        self.dtEdit.setCalendarPopup(True)

        # 设置日历控件
        self.dtEdit.setCalendarWidget(QCalendarWidget())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDateTimeEditInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())