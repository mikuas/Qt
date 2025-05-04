import sys

from typing import overload


from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QTextBrowser
from PySide6.QtCore import QMargins, QMarginsF, Qt
from PySide6.QtGui import QPainter, QColor

# from Interface import WidgetInterface
from .Interface import WidgetInterface


class Margins(QMargins):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, left: int, top: int, right: int, bottom: int): # QMarginsF: Args: left: float, top: float, right: float, bottom: float
        """_summary_

        Args:
            left (int): 左边距
            top (int): 顶部边距
            right (int): 右边距
            bottom (int): 底部边距
        """
        ...
    
    
class Function(QMarginsF):
    # 获取页面边距是否为空
    def isNull(self) -> bool:
        return super().isNull()
    ...


class W(WidgetInterface):
    def __init__(self, parent=None):
        super().__init__(parent, True, True)
        self._parent = parent
        self._parent.setContentsMargins(QMargins(10, 10, 10, 10))
        self.box.setContentsMargins(0, 0, 0, 0)
        
        self.button.setText('click me set margins')
        self.button.clicked.connect(self.updateMargin)
        
        self.edit.setPlaceholderText("设置内容边距, 用逗号隔开(left, top, right, bottom), 不写默认为0")
        
        self.box.addWidget(self.edit)
        self.box.addWidget(self.button)
        self.box.addWidget(self.getDialogBtn)
        self.box.addWidget(self.infos)
        
        self.initGetDialog()
    
    def initGetDialog(self):
        texts = [
            "获取顶部边距",
            "获取底部边距",
            "获取右边距",
            "获取左部边距"
        ]
        functions = [
            lambda: {
                self.infos.append(f"顶部边距为: {self._parent.contentsMargins().top()}")
            },
            lambda: {
                self.infos.append(f"底部边距为: {self._parent.contentsMargins().bottom()}")
            },
            lambda: {
                self.infos.append(f"右边距为: {self._parent.contentsMargins().right()}")
            },
            lambda: {
                self.infos.append(f"左部边距为: {self._parent.contentsMargins().left()}")
            }
        ]
        for text, function in zip(texts, functions):
            hBox = QHBoxLayout()
            self.getDialog.box.addLayout(hBox)
            hBox.addWidget(QLabel(text))
            button = QPushButton(text[:2])
            button.clicked.connect(function)
            hBox.addWidget(button)
    
    def updateMargin(self):
        text = self.edit.text()
        if text:
            text = text.split(',')
            text = [int(char) for char in text]
            lenght = len(text)
            if lenght < 5:
                for _ in range(4 - lenght):
                    text.append(0)
            self.infos.append(f"已设置内容边距: left: {text[0]}, top: {text[1]}, right: {text[2]}, bottom: {text[3]}")
            self._parent.setContentsMargins(QMargins(*text))
            
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor("deeppink"))
        painter.drawRoundedRect(self.rect(), 8, 8)


class QMarginInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.box = QVBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.widget = W(self)
        
        self.box.addWidget(self.widget)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMarginInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
    ...