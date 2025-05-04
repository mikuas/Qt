import sys
from typing import overload

from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLineEdit, QDialog, QLabel
from PySide6.QtCore import QPoint, QPointF, QPropertyAnimation, QSize, QSizeF
from PySide6.QtGui import QFont, QColor, Qt, QPainter

# from Interface import WidgetInterface
from .Interface import WidgetInterface


class Color(QColor):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, name: str):
        """_summary_

        Args:
            name (str): 颜色英文单词
        """
        ...
    @overload
    def __init__(self, c: Qt.GlobalColor): ...
    @overload
    def __init__(self, r: int, g: int, b: int, a: int = 255): ...
    @overload
    def __init__(self, rgb: int): ...
    

class Demo(WidgetInterface):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(
            """
            QTextBrowser {
                background: transparent;
            }
            """
        )
        self.button.deleteLater()
        
        self.color =  QColor('white')
        self.box.addWidget(self.infos)
    
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setPen(Qt.PenStyle.NoPen)    
        painter.setBrush(self.color)
        painter.drawRect(self.rect())
    
    
class QColorInterface(WidgetInterface):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.infos.deleteLater()
        self.box.setContentsMargins(50, 50, 50, 50)
        self.w = Demo(self)
        
        self.rl = QLineEdit(self)
        self.rl.setFixedHeight(35)
        self.rl.setPlaceholderText("设置RGB的R值, 不写默认为255")
        
        self.gl = QLineEdit(self)
        self.gl.setFixedHeight(35)
        self.gl.setPlaceholderText("设置RGB的G值, 不写默认为255")
        
        self.bl = QLineEdit(self)
        self.bl.setFixedHeight(35)
        self.bl.setPlaceholderText("设置RGB的B值, 不写默认为255")
        
        self.al = QLineEdit(self)
        self.al.setFixedHeight(35)
        self.al.setPlaceholderText("设置alpha通道的值, 不写默认为255")
        
        self.button.setText("apply")
        self.button.clicked.connect(self.updateRGB)
        
        self.gbtn = QPushButton("get RGBA value", self)
        self.gbtn.clicked.connect(lambda: self.w.infos.append(f"RGBA值为 {self.w.color.getRgb()}\n----------------------------------"))
        
        self.box.addWidget(self.rl)
        self.box.addWidget(self.gl)
        self.box.addWidget(self.bl)
        self.box.addWidget(self.al)
        self.box.addWidget(self.button)
        self.box.addWidget(self.gbtn)
        self.box.addWidget(self.w)
    
    def updateRGB(self):
        r = self.verify(self.rl.text())
        g = self.verify(self.gl.text())
        b = self.verify(self.bl.text())
        a = self.verify(self.al.text())
        self.w.color.setRgb(r, g, b, a)
        self.w.infos.append(f"已设置R值: {r}\n已设置G值: {g}\n已设置B值: {b}\n已设置A值: {a}\n-----------------")
        self.w.update()
    
    def verify(self, c):
        try:
            c = int(c)
            if c > 255:
                return 255
            return c
        except ValueError:
            return 255
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QColorInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())