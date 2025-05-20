# coding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

from qframelesswindow import AcrylicWindow, FramelessWindow


class Window(FramelessWindow):
    def __init__(self):
        super().__init__()

        self.windowEffect.setMicaEffect(self.winId(), isAlt=True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 520)
    window.windowEffect.setMicaEffect(window.winId(), isAlt=True)
    window.show()
    sys.exit(app.exec())