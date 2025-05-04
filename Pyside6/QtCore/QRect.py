import sys

from typing import overload

from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextBrowser
from PySide6.QtCore import QRect, QRectF, QPoint
from PySide6.QtGui import Qt, QColor, QPainter

# from Interface import WidgetInterface
from .Interface import WidgetInterface


class Rect(QRect):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, left: int, top: int, width: int, height: int):
        """_summary_

        Args:
            left (int): 离左边的距离
            top (int): 离右边的距离
            width (int): 宽度
            height (int): 高度
        """
        ...

    # 返回左上角 x 和 y 的值
    def x(self):
        return super().x()

    def y(self):
        return super().y()

    # 左下角 QPoint 和 右下角 QPoint
    def bottomLeft(self) -> QPoint:
        return super().bottomLeft()
    
    def bottomRight(self) -> QPoint:
        return super().bottomRight()

    # 返回中心点
    def center(self) -> QPoint:
        return super().center()

    # 平移
    def translate(self, p: QPoint) -> None: # dx: int, dy: int
        super().translate(p)
        
        
class QRectInterface(WidgetInterface):
    def __init__(self, parent=None):
        super().__init__(parent, True, True)
        self.button.setText('Apply')
        
        self.edit.setPlaceholderText("设值rect(左,上,宽,高,用逗号隔开,不写默认为0)")
        
        self.button.clicked.connect(self.updateRect)
        self.box.addWidget(self.edit)
        self.box.addWidget(self.button)
        self.box.addWidget(self.getDialogBtn)
        self.box.addWidget(self.infos)
        
        self._rect = QRect(self.rect())
        self.initGetDialog()
    
    def initGetDialog(self):
        texts = [
            "获取左上角QPoint",
            "获取右上角QPoint",
            "获取左下角QPoint",
            "获取右下角QPoint",
            "获取中心点QPoint"
        ]
        functions = [
            lambda: {
                self.infos.append(f"左上角QPoint为: {self._rect.topLeft()}")
            },
            lambda: {
                self.infos.append(f"右上角QPoint为: {self._rect.topRight()}")
            },
            lambda: {
                self.infos.append(f"左下角QPoint为: {self._rect.bottomLeft()}")
            },
            lambda: {
                self.infos.append(f"右下角QPoint为: {self._rect.bottomRight()}")
            },
            lambda: {
                self.infos.append(f"中心点QPoint为: {self._rect.center()}")
            }
        ]
        for text, function in zip(texts, functions):
            hBox = QHBoxLayout()
            self.getDialog.box.addLayout(hBox)
            hBox.addWidget(QLabel(text))
            button = QPushButton(text[:2])
            button.clicked.connect(function)
            hBox.addWidget(button)
        
    def updateRect(self):
        text = self.edit.text()
        if text:
            text = text.split(',')
            text = [int(char) for char in text]
            lenght = len(text)
            if lenght < 5:
                for _ in range(4 - lenght):
                    text.append(0)
            self.infos.append(f"设置rect, 距离顶部距离: {text[0]}, 顶部距离: {text[1]}, 宽度: {text[2]}, 高度: {text[3]}")
            self._rect.setRect(*text)
            self.update()
        
        
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor("deepskyblue"))
        painter.drawRect(self._rect)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRectInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())