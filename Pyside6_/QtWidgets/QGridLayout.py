# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar

from Interface import WidgetInterface


class QGridLayoutInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        """
        表单布局
        """
        self.button.deleteLater()
        self.infos.deleteLater()

        self.gridLayout = QGridLayout(self)
        self.box.addLayout(self.gridLayout)

        # 在第一列的末尾添加控件
        self.gridLayout.addWidget(QLabel("Hello", self))

        # 在指定的行列添加控件
        self.gridLayout.addWidget(QLabel("World", self), 3, 3, Qt.AlignmentFlag.AlignHCenter)

        # 设置控件的水平间距
        self.gridLayout.setHorizontalSpacing(10)
        # 设置控件的垂直间距
        self.gridLayout.setVerticalSpacing(10)

        # 获取行 | 列
        print(self.gridLayout.rowCount(), self.gridLayout.columnCount())

        # 设置行最小高度
        self.gridLayout.setRowMinimumHeight(0, 100)
        # 设置列最小宽度
        self.gridLayout.setColumnMinimumWidth(0, 100)

        print(self.gridLayout.cellRect(1, 1))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QGridLayoutInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())