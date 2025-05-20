# coding:utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter, QBrush, QPixmap, QTransform, QGradient


class QBurshDemo(QWidget):
    def __init__(self):
        super().__init__()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # 设置风格
        bursh = QBrush()
        bursh.setStyle(Qt.BrushStyle.VerPattern)
        print(f"Style: {bursh.style()}")
        
        # 设置纹理图片
        bursh.setTexture((QPixmap(r"C:\Users\Administrator\Qt\Pyside6_\_demo_\images\53.jpg")))
        
        # 设置颜色
        bursh.setColor(QColor("deeppink"))
        
        # 获取渐变色
        print(bursh.gradient())
        
        # 设置变换矩阵
        # bursh.setTransform(QTransform.TransformationType.TxRotate)
        
        print(f"是否不透明: {bursh.isOpaque()}")
        
        painter.setBrush(bursh)
        
        painter.drawRect(self.rect())
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, "QBrush Demo")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QBurshDemo()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())