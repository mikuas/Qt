# coding:utf-8

import sys

from PySide6.QtGui import QFont, Qt, QTextCharFormat, QTextDocument, QColor, QTextImageFormat, QIcon, QAction
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QScrollArea, QVBoxLayout, QLabel, QLineEdit, \
    QPushButton, QComboBox, QScrollBar, QSlider, QDial, QMenu, QCheckBox

from PySide6.QtCore import qDebug, QDate

from Interface import WidgetInterface


class QDateInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        date = QDate()

        # 根据年月日设置日期
        print(date.setDate(2023, 1, 1))

        print(date.weekNumber())

        # 获取记录的年月日
        print(date.getDate())

        # 返回增加指定天后的日期,可以为负数
        print(date.addDays(-11))
        # 返回增加指定月后的日期,可以为负数
        print(date.addMonths(-1))
        # 返回增加指定年后的日期,可以为负数
        print(date.addYears(-1))

        date.addDays(11)

        # 获取记录日期到指定日期天数
        print(date.daysTo(QDate(2023, 1, 5)))

        print(date.dayOfWeek())

        # 获取系统日期
        print(date.currentDate())

        # 获取当前日期
        print(date.currentDate())

        # print(date.fromString('1/1/1', Qt.DateFormat.DefaultLocaleShortDate))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDateInterface()
    window.resize(800, 520)
    window.show()
    window.close()
    # sys.exit(app.exec())