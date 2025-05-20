# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar

from Interface import WidgetInterface



class QScrollAreaInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.scroll = QScrollArea(self)
        self.box.addWidget(self.scroll)

        self.widget = QWidget()

        self.scroll.setWidget(self.widget)

        self.widgetLayout = QVBoxLayout(self.widget)
        self.widget.setLayout(self.widgetLayout)

        for _ in range(100):
            self.widgetLayout.addWidget(QLabel("Hello World" + str(_)))

        # 设置内容控件是否可以调节尺寸
        self.scroll.setWidgetResizable(True)

        # 设置滚动条策略
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QScrollAreaInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
