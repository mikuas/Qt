# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar

from Interface import WidgetInterface


class QStackedWidgetInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.hbox = QHBoxLayout()

        self.stackedWidget = QStackedWidget(self)
        self.box.addWidget(self.stackedWidget)

        self.box.addLayout(self.hbox)
        font = QFont("微软雅黑", 64)

        # 添加窗口
        for _ in range(10):
            label = QLabel(str(_ + 1) + "_page")
            label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
            label.setFont(font)
            self.stackedWidget.addWidget(label)

        # 设置当前窗口
        # self.stackedWidget.setCurrentWidget()
        # self.stackedWidget.setCurrentIndex()

        # 获取当前窗口
        print(self.stackedWidget.currentWidget())

        # 获取指定窗口索引值
        print(self.stackedWidget.indexOf(self.stackedWidget.currentWidget()))

        # 移除窗口
        # self.stackedWidget.removeWidget()

        # 获取窗口数量
        print(self.stackedWidget.count())


        self.up = QPushButton('<-')
        self.next = QPushButton('->')
        self.up.clicked.connect(lambda: self.pageUpdate(True))
        self.next.clicked.connect(lambda: self.pageUpdate(False))

        self.hbox.addWidget(self.up)
        self.hbox.addWidget(self.next)

    def pageUpdate(self, isUp: bool):
        index = self.stackedWidget.currentIndex()
        if isUp:
            self.stackedWidget.setCurrentIndex(index - 1 if index > 0 else index)
        else:
            self.stackedWidget.setCurrentIndex(index + 1 if index < self.stackedWidget.count() - 1 else index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QStackedWidgetInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())

