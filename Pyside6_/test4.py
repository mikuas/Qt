# coding:utf-8
import sys

from FluentWidgets import FluentWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QApplication, QWidget

from qframelesswindow import FramelessWindow, AcrylicWindow, WindowEffect


class Window(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 520)

        # self.updateFrameless()
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.CustomizeWindowHint)
        self.setWindowFlags(Qt.WindowType.CustomizeWindowHint)
        self.titleBar.setStyleSheet('background-color: orange;')

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.windowEffect = WindowEffect(self)
        self.windowEffect.enableBlurBehindWindow(self.winId())
        self.windowEffect.addWindowAnimation(self.winId())
        self.windowEffect.setMicaEffect(self.winId(), isAlt=True)
        # self.windowEffect.setAcrylicEffect(self.winId(), 'F2F2F290')

        # self.updateFrameless()

    def updateFrameless(self):
        """ update frameless window """
        # self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        # add DWM shadow and window animation
        self.windowEffect.addWindowAnimation(self.winId())
        if not isinstance(self, AcrylicWindow):
            self.windowEffect.addShadowEffect(self.winId())

    # def paintEvent(self, event):
    #     super().paintEvent(event)
    #     painter = QPainter(self)
    #     painter.setPen(Qt.NoPen)
    #     painter.setBrush(QColor('deeppink'))
    #     painter.drawRect(self.rect())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())