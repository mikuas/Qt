# coding:utf-8
import sys

from PySide6.QtCore import QRectF
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QImage, QPainter, Qt, QPainterPath


class Window(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing | QPainter.LosslessImageRendering | QPainter.SmoothPixmapTransform)
        painter.setPen(Qt.NoPen)
        path = QPainterPath()
        rect = QRectF(self.rect())
        path.addRoundedRect(rect, 8, 8)
        painter.setClipPath(path)
        painter.drawImage(rect, QImage(r"images/53.jpg"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())