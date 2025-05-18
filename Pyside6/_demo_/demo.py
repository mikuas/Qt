# coding:utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout
from PySide6.QtGui import Qt, QPainter, QColor

from qframelesswindow import FramelessWindow
from qfluentwidgets import FluentWindow, MSFluentWindow, SplitFluentWindow, ComboBox, SplitTitleBar


class LeftWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor("skyblue"))
        painter.drawRect(self.rect())


class RightWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor('orange'))
        painter.drawRect(self.rect())


class Window(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.setTitleBar(SplitTitleBar(self))
        
        self.windowEffect.setMicaEffect(self.winId(), isAlt=True)
        
        self.box = QHBoxLayout(self)
        self.box.setContentsMargins(0,0,0,0)
        self.setContentsMargins(0,0,0,0)
        
        self.box.addWidget(LeftWidget(self))
        self.box.addWidget(RightWidget(self))
        
        self.titleBar.raise_()
    
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor('deeppink'))
        painter.drawRect(self.rect())
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 520)
    window.windowEffect.setMicaEffect(window.winId(), isAlt=True)
    window.show()
    sys.exit(app.exec())