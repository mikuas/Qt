# coding:utf-8

import sys

from PySide6.QtCore import QRect
from PySide6.QtGui import QFont, Qt, QTextCharFormat, QTextDocument, QColor, QTextImageFormat, QIcon, QAction, QPainter
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QScrollArea, QVBoxLayout, QLabel, QLineEdit, \
    QPushButton, QComboBox, QScrollBar, QSlider, QStyle, QStyleOptionSlider

from Interface import WidgetInterface

from qfluentwidgets import Slider


class ValueSlider(QSlider):
    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super().__init__(orientation, parent)

    def paintEvent(self, event):
        super().paintEvent(event)

        opt = QStyleOptionSlider()
        self.initStyleOption(opt)

        # 获取 handle 的矩形区域
        handle_rect = self.style().subControlRect(
            QStyle.CC_Slider,
            opt,
            QStyle.SC_SliderHandle,
            self
        )

        value_text = str(self.value())
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setFont(QFont("Arial", 10))
        painter.setPen(QColor(50, 50, 50))

        text_width = painter.fontMetrics().horizontalAdvance(value_text)
        text_height = 20
        padding = 6

        # 显示在滑块右边
        x = handle_rect.right() + padding
        y = handle_rect.center().y() - text_height // 2

        # 可选：圆角背景框
        painter.setBrush(QColor(255, 255, 255, 220))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(QRect(x - 4, y - 2, text_width + 8, text_height), 6, 6)

        # 画数字
        painter.setPen(QColor(30, 30, 30))
        painter.drawText(QRect(x, y, text_width + 4, text_height), Qt.AlignCenter, value_text)

        painter.end()


class QScrollBar_QSlider_Interface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.scrollBar = QScrollBar(self)
        self.slider = ValueSlider(self)

        # 设置控件方向
        self.scrollBar.setOrientation(Qt.Horizontal)

        # 获取方向
        print(self.scrollBar.orientation())

        self.slider.setMaximum(100)
        self.slider.setMinimum(0)

        self.slider.setSingleStep(1)

        # 设置滑块位置
        self.slider.setSliderPosition(50)

        # 设置滑块两个刻度之间的值, 用于QSlider
        self.slider.setTickInterval(24)

        # self.scrollBar.setInvertedControls(True)

        self.box.addWidget(self.scrollBar)
        self.box.addWidget(self.slider)

        self.slider.valueChanged.connect(lambda value: print(value))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QScrollBar_QSlider_Interface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
    ...