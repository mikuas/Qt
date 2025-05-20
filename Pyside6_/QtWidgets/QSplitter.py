# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar

from Interface import WidgetInterface


class QSplitterInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.splitter = QSplitter(self)

        self.box.addWidget(self.splitter)

        # 在末尾添加控件
        self.splitter.addWidget(QLabel("Hello World"))

        self.splitter.setSizes([100, 100, 100])

        self.splitter.setStyleSheet("""
            QSplitter::handle {
                background-color: gray;
                border-radius: 8px;
            }
        """)


        # 替换指定索引控件
        self.splitter.replaceWidget(0, QLabel("Ciallo World"))

        # 设置分割方向
        self.splitter.setOrientation(Qt.Orientation.Horizontal)

        self.splitter.addWidget(QLabel("Hello World"))

        # 设置分割条宽度
        self.splitter.setHandleWidth(5)

        # 设置内部控件是否可以折叠 默认 True
        self.splitter.setChildrenCollapsible(False)

        self.splitter.addWidget(QLabel("Ciallo World"))
        self.splitter.addWidget(QLabel("Log World"))
        self.splitter.addWidget(QLabel("Echo World"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QSplitterInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())