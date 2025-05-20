# coding:utf-8
import random
import re
import sys

from FluentWidgets import themeColor
from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction, QIcon, QDesktopServices
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar, QToolButton
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar, QSize, QUrl

from Interface import WidgetInterface


class QToolButtonInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QIcon(r"C:\Users\Administrator\OneDrive\Pictures\微信图片_20250501162545.jpg"))
        self.toolButton.setIconSize(QSize(32, 32))
        self.toolButton.setAutoRaise(True)
        self.toolButton.setArrowType(Qt.ArrowType.DownArrow)

        self.toolButton.setFixedSize(256, 35)
        self.box.addWidget(self.toolButton, 1, alignment=Qt.AlignmentFlag.AlignHCenter)

        print(themeColor().toTuple())

        self.label = QLabel('<a href="https://www.qt.io">点击访问 Qt 官网</a>')
        self.label.setOpenExternalLinks(False)
        self.label.setStyleSheet(
            """
            QLabel a {
                color: deeppink;
            }
            QLabel a:hover {
                color: deepskyblue;
            }
            """
        )
        self.label.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.label.linkActivated.connect(self.onClick)
        self.label.setFont(QFont("微软雅黑", 32))
        self.box.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignHCenter)

    def onClick(self):
        links = re.findall(r'href=[\'"]([^\'"]+)[\'"]', self.label.text())
        url = QUrl(links[0])
        if url.isValid():
            QDesktopServices.openUrl(url)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QToolButtonInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
