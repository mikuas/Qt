# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar

from Interface import WidgetInterface


class QCalendarInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.calendarWidget = QCalendarWidget(self)

        self.box.addWidget(self.calendarWidget)

        # 设置选中日期
        self.calendarWidget.setSelectedDate(QDate().currentDate())

        # 获取选中日期
        print(self.calendarWidget.selectedDate())

        # 设置日历
        self.calendarWidget.setCalendar(QCalendar())
        # 获取日历
        print(self.calendarWidget.calendar())

        # 设置表的样式
        tf = QTextCharFormat()
        tf.setForeground(QColor(Qt.blue))
        self.calendarWidget.setDateTextFormat(QDate().currentDate(), tf)

        # 设置是否显示网格线
        self.calendarWidget.setGridVisible(False)

        # 设置水平表头的格式
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.HorizontalHeaderFormat.SingleLetterDayNames)

        # self.calendarWidget.setVerticalHeaderFormat()

        # 设置日历控件可以选择的最小和最大日期
        self.calendarWidget.setDateRange(QDate(2023, 1, 1), QDate(2023, 12, 31))

        # 设置导航条是否可见
        self.calendarWidget.setNavigationBarVisible(False)

        # 显示已选中的日期
        self.calendarWidget.showSelectedDate()

        # 获取日历显示的年份
        self.calendarWidget.yearShown()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QCalendarInterface()
    window.show()
    sys.exit(app.exec())