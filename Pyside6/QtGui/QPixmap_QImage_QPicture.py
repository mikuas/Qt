import sys

from typing import overload


from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import QSize, QRect, QIODevice
from PySide6.QtGui import QPixmap, QImage, QIcon

# from Interface import WidgetInterface
from .Interface import WidgetInterface


class Pixmap(QPixmap):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, w: int, h: int): ...
    @overload 
    def __init__(self, s: QSize): ...
    @overload
    def __init__(self, s: str): ...
    @overload
    def __init__(self, i: QImage): ...
    
    # 深度复制图像的局部区域
    def copy(self, rect: QRect): ...
    def copy(self, x: int, y: int, width: int, height: int): ...
    
    # 从文件中加载图像, 成功返回 True
    def load(self, fileName, format = ..., flags = ...):
        return super().load(fileName, format, flags)

    # 保存图像到设备中, 成功返回 True
    @overload
    def save(self, device: QIODevice, format: str | None= ..., quality: int = ...) -> bool: ...
    @overload
    def save(self, fileName: str, format: str | None= ..., quality: int = ...) -> bool: ...

    # 缩放图像
    def scaled(self): ...
    
    # 用某种颜色填充图像
    def fill(self, fillColor = ...):
        return super().fill(fillColor)
    

class Image(QImage):
    
    # 设置指定位置处的颜色
    def setPixelColor(self): ...
    
    # 获取指定位置处的颜色值
    def pixelColor(self): ...
    
    # 颜色反转
    def rgbSwap(self):
        return super().rgbSwap()
    
    # 返回颜色反转后的 QImage
    def rgbSwapped(self):
        return super().rgbSwapped()
    
    # 对图像进行变换
    def transformed(self, matrix, mode = ...):
        return super().transformed(matrix, mode)
    
    # 对图像进项镜像操作
    def mirror(self, horizontally = ..., vertically = ...):
        return super().mirror(horizontally, vertically)
    ...


class QPixmapQImageQPictureInterface(WidgetInterface):
    def __init__(self, parent=None):
        super().__init__(parent, True)
        self._pixmap = QPixmap()
        
        self.button.setText("")
        
        self.loadBtn = QPushButton("load", self)
        self.loadBtn.clicked.connect(self.load)
        
        self.saveBtn = QPushButton("save", self)
        self.saveBtn.clicked.connect(self.save)
        
        self.box.addWidget(self.edit)
        self.box.addWidget(self.button)
        self.box.addWidget(self.loadBtn)
        self.box.addWidget(self.saveBtn)
        self.box.addWidget(self.infos)
        

    def load(self):
        print(self._pixmap.load(r"C:\Users\Administrator\Pictures\Snipaste_2025-03-30_14-07-11.png"))

    def save(self):
        print(self._pixmap.save(r"C:\Users\Administrator\Pictures\Snipaste_2025-03-30_14-07-11.png", r"C:\test.jpg"))

    def verify(self, point):
        try:
            return int(point)
        except ValueError:
            return 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QPixmapQImageQPictureInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
    ...