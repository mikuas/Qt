# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar

from Interface import WidgetInterface


class QHBoxLayout_QVBoxLayout_Interface(WidgetInterface):
    def __init__(self):
        super().__init__()
        """
        表单布局
        """
        self.button.deleteLater()
        self.infos.deleteLater()
        self.box = QVBoxLayout(self)

        # 添加控件
        self.box.addWidget(QLabel("Hello", self), 0, Qt.AlignmentFlag.AlignHCenter)

        # 获取最大尺寸
        print(self.box.maximumSize())

        # 设置布局方向
        self.box.setDirection(QBoxLayout.Direction.Down)

        # 设置控件随窗口尺寸改变时的变化方式
        self.box.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QHBoxLayout_QVBoxLayout_Interface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())