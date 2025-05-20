# coding:utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPen, QColor, QPainter, QBrush
from PySide6.QtCore import Qt, QPointF


class Pen(QPen):
    def __init__(self):
        super().__init__()
        
        # 设置线条样式
        self.setStyle(Qt.PenStyle.SolidLine)
        """PenStyle
        
        NoPen               不绘制线条
        SoldLine            实线
        DashLine            虚线
        DotLine             点线
        DashDotLine         点画线
        DashNotDotLine      双点画线      
        CustomDashLine      自定义线
        """
        
        # 设置线条宽度
        self.setWidth(5)
        
        # 获取线条是否是实线填充
        print(self.isSolid())
        
        # 设置画刷
        self.setBrush(QColor("skyblue"))
        
        # 设置线端部样式
        self.setCapStyle(Qt.PenCapStyle.RoundCap)
        
        # 设置颜色
        self.setColor('deeppink')
        
        # 设置是否进行装饰
        self.setCosmetic(True)
        
        # 设置虚线开始绘制的点与线起始点的距离
        self.setDashOffset(0.5)
        
        # 设置用户自定义虚线样式
        self.setDashPattern([4, 2, 4, 2]) # 线, 间隔
        
        # 设置两相交线连接点处的样式
        self.setJoinStyle(Qt.PenJoinStyle.MiterJoin)
         
        self.setMiterLimit(10)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Pen())
        painter.drawLine(0, self.height()/2-5, self.width(), self.height()/2-5)
        
        # 绘制折线
        painter.drawPolyline([
            QPointF(10, 10), QPointF(-20, 30), QPointF(30, 50), QPointF(-40, 70)
        ])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())