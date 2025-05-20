# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar

from Interface import WidgetInterface


class QGroupBoxInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.groupBox = QGroupBox("GroupBox", self)

        self.box.addWidget(self.groupBox)

        self.groupLayout = QHBoxLayout()
        self.groupLayout.addWidget(QLabel("Ciallo"))
        self.groupLayout.addWidget(QLabel("World"))

        self.groupBox.setLayout(self.groupLayout)

        # 获取标题名称
        print(self.groupBox.title())

        # 设置是否处于扁平状态
        # self.groupBox.setFlat(True)

        # 设置标题栏上是否有勾选选项
        self.groupBox.setCheckable(True)

        # 获取是否处于勾选状态
        print(self.groupBox.isChecked())

        # 设置标题栏对齐方式
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignHCenter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QGroupBoxInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())