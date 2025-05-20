# coding:utf-8
import random
import re
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction, QIcon, QDesktopServices, \
    QKeySequence
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar, QSize, QUrl, QRect, QEvent, QEventLoop, \
    QChildEvent, QTimerEvent, QWinEventNotifier, QAbstractNativeEventFilter, QAbstractEventDispatcher, \
    QDynamicPropertyChangeEvent, QMimeData, QByteArray
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar, QToolButton, QStatusBar, QMainWindow, QDockWidget, QDialog, QMdiArea, QMdiSubWindow, QFontDialog, \
    QColorDialog, QFileDialog, QInputDialog, QMessageBox, QErrorMessage, QProgressDialog, QWizard, QWizardPage, QStyle

from Interface import WidgetInterface


class QMimeDataInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.infos.deleteLater()
        self.button.deleteLater()

        self.mimeData = QMimeData()

        # 移除格式
        # self.mimeData.removeFormat("text/plain")

        # 设置颜色数据
        self.mimeData.setColorData('RED')
        # 获取是否有颜色数据
        print(self.mimeData.hasColor())
        # 获取颜色数据
        print(self.mimeData.colorData())

        # 设置HTML数据
        self.mimeData.setHtml('<h1>hello world</h1>')
        print(self.mimeData.hasHtml())
        print(self.mimeData.html())

        # 设置图像数据
        self.mimeData.setImageData(r"C:\Users\Administrator\Default.png")
        print(self.mimeData.hasImage())
        print(self.mimeData.imageData())

        # 设置文本数据
        self.mimeData.setText('Hello World')
        print(self.mimeData.hasText())
        print(self.mimeData.text())

        # 设置URL数据
        self.mimeData.setUrls(['https://www.baidu.com', 'https://www.bilibili.com', 'https://www.google.com'])
        print(self.mimeData.hasUrls())
        print(self.mimeData.urls(), '\n', [url.url() for url in self.mimeData.urls()])

        # 设置某种格式的数据
        self.mimeData.setData('ciallo', QByteArray("Ciallo World"))
        print(self.mimeData.data('ciallo'))
        print(self.mimeData.hasFormat('ciallo'), self.mimeData.hasFormat('none'))

        # 清空格式和数据
        self.mimeData.clear()

        # 获取格式列表
        print(self.mimeData.formats(), '\n', [f.split('-')[-1] for f in self.mimeData.formats()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMimeDataInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
