import sys

from typing import overload


from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import QSize, QRect, QIODevice, QPoint
from PySide6.QtGui import QPixmap, QImage, QIcon, QPainter, Qt

# from Interface import WidgetInterface
from .Interface import WidgetInterface


class QIconInterfac(WidgetInterface):
    def __init__(self, parent=None, enit=True, dbtn=False):
        super().__init__(parent, enit, dbtn)
        self.edit.setPlaceholderText("输入图片路径")
        
        self.pixmap = QPixmap(self.width(), self.height())
        
        self.button.setText("Apply")
        self.button.clicked.connect(self.updateIcon)
        
        self.icon = QIcon(self.pixmap)

        self.setWindowIcon(self.icon)
        
        self.box.addWidget(self.edit)
        self.box.addWidget(self.button)
        self.box.addWidget(self.infos)
    
    def updateIcon(self):
        self.pixmap.load(self.edit.text())
        self.update()
    
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter()
        # painter.setPen(Qt.PenStyle.NoPen)
        painter.drawPixmap(QPoint(0, 0), self.pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QIconInterfac()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
    ...