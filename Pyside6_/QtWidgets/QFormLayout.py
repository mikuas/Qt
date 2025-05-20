# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar

from Interface import WidgetInterface


class QFormLayoutInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        """
        表单布局
        """
        self.button.deleteLater()
        self.infos.deleteLater()
        self.box.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.formLayout = QFormLayout(self)

        # 末尾添加行, 分别在左右
        self.formLayout.addRow("姓名", QLabel("张三"))
        self.formLayout.addRow(QLabel("Ciallo"), QLabel("World"))

        self.formLayout.addRow(QDateTimeEdit(self))

        # 设置左列的对其方式
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        # 设置控件在表单布局中的对其方法
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.box.addLayout(self.formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QFormLayoutInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())