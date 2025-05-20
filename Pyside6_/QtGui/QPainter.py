# coding:utf-8

import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainterPath, QPainter, QColor, QPen
from PySide6.QtCore import Qt, QPointF

from math import sin, cos, tan, pi


class Window(QWidget):
    def __init__(self):
        super().__init__()

    # def paintEvent(self, event):
    #     painter = QPainter(self)
    #     font = painter.font()
    #     font.setPixelSize(20)
    #     painter.setFont(font)
        
    #     painter.setRenderHints(QPainter.RenderHint.TextAntialiasing | QPainter.RenderHint.Antialiasing)
        
    #     pen = QPen()
    #     pen.setWidth(5)
    #     painter.setPen(pen)
        
    #     r = 100
    #     x = self.width() / 2
    #     y = self.height() / 2
    #     p1 = QPointF(r * cos(-90 * pi / 180,) + x, r * sin(-90 * pi / 180,) + y)
    #     p2 = QPointF(r * cos(-18 * pi / 180,) + x, r * sin(-18 * pi / 180,) + y)
    #     p3 = QPointF(r * cos(54 * pi / 180,) + x, r * sin(54 * pi / 180,) + y)
    #     p4 = QPointF(r * cos(126 * pi / 180,) + x, r * sin(126 * pi / 180,) + y)
    #     p5 = QPointF(r * cos(198 * pi / 180,) + x, r * sin(198 * pi / 180,) + y)
        
    #     painter.drawPolyline([p1, p2, p3, p4, p5, p1])
    #     painter.drawText(p1, "p1")
    #     painter.drawText(p2, "p2")
    #     painter.drawText(p3, "p3")
    #     painter.drawText(p4, "p4")
    #     painter.drawText(p5, "p5")
    
    def paintEvent(self, event):
        painter = QPainter(self)
        
        # 设置背景色, 只对不透明的文字,虚线或位图起作用
        painter.setBackground(QColor("deeppink"))
        
        # 设置透明或不透明背景模式
        painter.setBackgroundMode(Qt.BGMode.TransparentMode)
        
        # 设置画笔
        painter.setBrush(QColor("orange"))
        
        # 设置画刷起点
        painter.setBrushOrigin(0, 0)
        
        # 设置剪切路径
        # painter.setClipPath()
        
        # 设置剪切矩形区域
        painter.setClipRect(self.rect())
        
        # 设置剪切区域
        painter.setClipRegion(self.rect())
        
        # 设置是否自动剪切
        painter.setClipping(True)
        
        # 设置图形合成模式
        # painter.setCompositionMode()
        
        # 设置字体
        # painter.setFont()
        
        # 设置布局方向
        # painter.setLayoutDirection()
        
        # 设置不透明度
        painter.setOpacity(1)

        # 设置钢笔
        # painter.setPen()
        
        # 设置渲染模式
        painter.setRenderHints(QPainter.RenderHint.TextAntialiasing | QPainter.RenderHint.LosslessImageRendering)
        
        # 设置全局变换矩阵
        # painter.setTransform()
        # painter.setWorldTransform()
        
        # 设置是否自动启动视口变换
        painter.setViewTransformEnabled(True)
        
        # 设置视口
        painter.setViewport(self.rect())
        
        # 设置逻辑窗口
        # painter.setWindow()
        
        # 设置是否启动全局矩阵变换
        painter.setWorldMatrixEnabled(True)
        
        # 保存状态到堆栈
        painter.save()
        
        # 从堆栈中恢复状态
        painter.restore()
        
        # painter.drawRect(self.rect())
        
        painter.begin()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())