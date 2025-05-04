# coding:utf-8
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QLabel, QPushButton, QTabWidget, QTabBar, QApplication
)
from PySide6.QtCore import Qt
import sys


class CustomTab(QWidget):
    def __init__(self, text, parent, index):
        super().__init__(parent)
        self.setContentsMargins(0,0,0,0)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(4)

        self.update()

        self.setStyleSheet('background-color: red;')

        self.label = QLabel(text)
        layout.addWidget(self.label)

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter()
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor('deeppink'))
        painter.drawRect(self.rect())


class CustomTabWidget(QTabWidget):
    def __init__(self):
        super().__init__()

        self.setTabBar(QTabBar())

        for i in range(5):
            page = QLabel(f"内容页面 {i+1}")
            self.addTab(page, "")

            custom_tab = CustomTab(f"Tab{i+1}", self, i)
            self.tabBar().setTabButton(i, QTabBar.LeftSide, custom_tab)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CustomTabWidget()
    win.resize(600, 400)
    win.show()
    sys.exit(app.exec())
