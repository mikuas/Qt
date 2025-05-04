# coding:utf-8

import sys

from PySide6.QtGui import QFont, Qt, QTextCharFormat, QTextDocument, QColor, QTextImageFormat, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QScrollArea, QVBoxLayout, QLabel, QLineEdit, \
    QPushButton, QComboBox, QScrollBar, QSlider, QDial

from Interface import WidgetInterface


class QDialInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.dial = QDial(self)

        # 设置刻度是否可见
        self.dial.setNotchesVisible(True)
        # 设置刻度之间的距离
        self.dial.setNotchTarget(5)

        # 设置最大刻度和最小刻度是否重合
        self.dial.setWrapping(True)
        self.dial.setRange(0, 100)

        # 获取相邻刻度之间的值
        print(self.dial.notchSize())

        # 设置刻度反向
        self.dial.setInvertedAppearance(True)

        self.box.addWidget(self.dial)

        label = QLabel(self)

        self.box.addWidget(label, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.dial.valueChanged.connect(lambda value: label.setText(str(value)))

        self.box.setAlignment(Qt.AlignmentFlag.AlignTop)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDialInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
    ...