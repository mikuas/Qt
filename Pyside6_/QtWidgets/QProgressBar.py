# coding:utf-8

import sys

from PySide6.QtGui import QFont, Qt, QTextCharFormat, QTextDocument, QColor, QTextImageFormat, QIcon, QPainter, \
    QLinearGradient
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QScrollArea, QVBoxLayout, QLabel, QLineEdit, \
    QPushButton, QComboBox, QScrollBar, QSlider, QDial, QProgressBar, QStyleOptionProgressBar

from PySide6.QtCore import QTimer, QRect

from Interface import WidgetInterface


class CustomProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRange(0, 100)
        self.setValue(0)

    def paintEvent(self, event):
        # 创建 QStyleOptionProgressBar 以获得进度条的各种信息
        opt = QStyleOptionProgressBar()
        self.initStyleOption(opt)

        # 先画背景
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 获取进度条的矩形区域
        rect = self.rect()

        # 背景颜色
        painter.setBrush(QColor(240, 240, 240))  # 背景色
        painter.drawRect(rect)

        # 获取 chunk 占用区域
        chunk_rect = QRect(rect.left(), rect.top(), int(rect.width() * self.value() / self.maximum()), rect.height())

        # 绘制进度条的 chunk
        gradient = QLinearGradient(chunk_rect.topLeft(), chunk_rect.topRight())
        gradient.setColorAt(0, QColor('pink'))  # 渐变开始颜色
        gradient.setColorAt(1, QColor('deeppink'))  # 渐变结束颜色

        painter.setBrush(gradient)
        painter.drawRect(chunk_rect)

        # 画进度文本
        painter.setPen(QColor(0, 0, 0))  # 文字颜色
        painter.drawText(rect, Qt.AlignCenter, f"{self.value()}%")
        painter.end()

class QProgressBarInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.timer = QTimer(self)

        self.timer.timeout.connect(lambda: {self.progressBar.setFormat(f'current value: {self.progressBar.value()}')
                                            , self.progressBar.setValue(self.progressBar.value() + 5)
                                            })

        self.timer.start(1000)

        self.progressBar = CustomProgressBar(self)

        self.progressBar.setStyleSheet(
            """
            QProgressBar {
                border: 2px solid #555;
                border-radius: 5px;
                height: 20px;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,stop:0 #66e, stop:1 #bbf);
            }
            """)

        # 设置显示文本
        self.progressBar.setTextVisible(True)
        self.progressBar.setFormat(f'value')

        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.progressBar.setValue(50)

        self.progressBar.setOrientation(Qt.Orientation.Horizontal)
        # self.progressBar.setInvertedAppearance(True)
        self.progressBar.setRange(0, 100)
        self.box.addWidget(self.progressBar)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QProgressBarInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
    ...