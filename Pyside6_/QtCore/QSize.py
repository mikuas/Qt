import sys
from typing import overload

from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLineEdit, QDialog, QLabel
from PySide6.QtCore import QPoint, QPointF, QPropertyAnimation, QSize, QSizeF

# from Interface import WidgetInterface
try:
    from .Interface import WidgetInterface
except ImportError:
    from Interface import WidgetInterface


class Size(QSize):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, w: int, h: int): # # QSizeF: Args: w: float, h: float
        """_summary_

        Args:
            w (int): 宽度
            h (int): 高度
        """
        ...


class QSizeInterface(WidgetInterface):
    def __init__(self, parent=None):
        super().__init__(parent, True, True)
        
        self.edit.setPlaceholderText("设置按钮的大小, 用逗号隔开(width,height), 不写默认为0")
        
        self.sizeBtn = QPushButton("SIZE BUTTON", self)
        self.sizeBtn.setStyleSheet("background: deeppink;")
        self.sizeBtn.move(self.width() / 2 - 100, self.height() / 2 - 100)
        
        self.button.setText("Change Size")
        self.button.clicked.connect(lambda: self.createPosAni(self.getSize()))
        
        self.box.addWidget(self.edit)
        self.box.addWidget(self.button)
        self.box.addWidget(self.getDialogBtn)
        self.box.addWidget(self.infos)
        
        self.posAni = QPropertyAnimation(self.sizeBtn, b'size', self)
        
        self.initGetDialog( )

    def initGetDialog(self): 
        texts = [
            "获取宽度",
            "获取高度",
            "获取高度和宽度是否为空(widtdh=height=0)",
            "对调宽度和高度轴"
        ]
        functions = [
            lambda: {
                self.infos.append(f"宽度: {self.sizeBtn.width()}")
            },
            lambda: {
                self.infos.append(f"高度: {self.sizeBtn.height()}")
            },
            lambda: {
                self.infos.append("宽度和高度为空" if self.sizeBtn.size().isNull() else "宽度和高度不为空")
            },
            lambda: {
                self.createPosAni(self.sizeBtn.size().transposed().toTuple()),
                self.infos.append(f"已对调X和Y轴, 结果为: Widtg: {self.sizeBtn.width()} | Height: {self.sizeBtn.height()}")
            }
        ]
        
        for t, f in zip(texts, functions):
            h = QHBoxLayout()
            self.getDialog.box.addLayout(h)
            h.addWidget(QLabel(t))
            b = QPushButton(t[:2])
            b.clicked.connect(f)
            h.addWidget(b)

    def createPosAni(self, targetSize):
        self.posAni.setDuration(1000)
        self.posAni.setStartValue(self.sizeBtn.size())
        currentSize = self.sizeBtn.size().toTuple()
        self.infos.append(f"按钮从 Width: {currentSize[0]} | Height: {currentSize[1]} 改变为了 Width: {targetSize[0]} | Height: {targetSize[1]}")
        self.posAni.setEndValue(QSize(*targetSize))
        self.posAni.start()
    
    def getSize(self):
        point = self.edit.text()
        if point:
            point = point.split(',')
            if len(point) >= 2:
                return [self.verify(point[0]), self.verify(point[1])]
            else:
                return [self.verify(point[0]), 0]
        return [0, 0]
    
    def verify(self, point):
        try:
            return int(point)
        except ValueError:
            return 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QSizeInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
    ...