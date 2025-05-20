# coding:utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QGradient, QPainter, QPixmap, QImage, QBrush,\
    QLinearGradient, QRadialGradient, QConicalGradient


class QGradientDemo(QWidget):
    def __init__(self):
        super().__init__()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        
        gradient = QGradient()
        # 线性, 径向, 圆锥渐变
        linearGradient = QLinearGradient(0, 0, 100, 100)
        radialGradient = QRadialGradient(50, 50, 50)
        conicalGradient = QConicalGradient(50, 50, 45)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QGradientDemo()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())