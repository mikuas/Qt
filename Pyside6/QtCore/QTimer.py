# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar

from Interface import WidgetInterface


class QTimerInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.timer = QTimer(self)

        # 设置发送信号的间隔
        self.timer.setInterval(1000)

        # 获取间隔
        print(self.timer.interval())

        # 获取定时器是否激活
        print(self.timer.isActive())

        # 获取距离下次发送信号的时间 毫秒
        print(self.timer.remainingTime())

        # 设置定时器是否单词发送
        self.timer.setSingleShot(True)

        # 设置定时器类型
        self.timer.setTimerType(Qt.TimerType.PreciseTimer)

        # 获取定时器id
        print(self.timer.timerId())

        # 经过 ** 毫秒后调用Python的可执行函数 Callable
        self.timer.singleShot(1000, lambda: print(True))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QTimerInterface()
    window.show()
    window.hide()
    sys.exit(app.exec())