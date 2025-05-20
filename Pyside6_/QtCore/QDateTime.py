# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate

from Interface import WidgetInterface


class QDateTimeInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.dateTime = QDateTime()

        # 设置日期
        self.dateTime.setDate(QDate().currentDate())
        # 设置时间
        self.dateTime.setTime(QTime().currentTime())

        # 获取日期
        print(self.dateTime.date())
        # 获取时间2
        print(self.dateTime.time())

        # 获取系统日期和时间
        print(self.dateTime.currentDateTime())
        # 获取世界统一时间
        print(self.dateTime.currentDateTimeUtc())

        # 设置从1970年1月1日0时开始的时间(秒)
        self.dateTime.setSecsSinceEpoch(0)

        # 返回1970年1月1日0时开始到现在的秒数
        print(self.dateTime.currentSecsSinceEpoch())

        print(self.dateTime.toSecsSinceEpoch())

        # 所记录的时间是否有效
        self.dateTime.isValid()

        # 获取指定日期时间的间隔
        print(self.dateTime.daysTo(QDateTime().currentDateTime()))

        print(self.dateTime.toLocalTime())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDateTimeInterface()
    window.show()
    window.hide()
    sys.exit(app.exec())