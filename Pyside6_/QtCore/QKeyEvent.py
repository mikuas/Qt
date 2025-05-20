# coding:utf-8
import random
import re
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction, QIcon, QDesktopServices, \
    QKeySequence
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar, QSize, QUrl, QRect, QEvent, QEventLoop, \
    QChildEvent, QTimerEvent, QWinEventNotifier, QAbstractNativeEventFilter, QAbstractEventDispatcher, \
    QDynamicPropertyChangeEvent
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar, QToolButton, QStatusBar, QMainWindow, QDockWidget, QDialog, QMdiArea, QMdiSubWindow, QFontDialog, \
    QColorDialog, QFileDialog, QInputDialog, QMessageBox, QErrorMessage, QProgressDialog, QWizard, QWizardPage, QStyle

from Interface import WidgetInterface


class QKeyEventInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.infos.deleteLater()
        self.button.deleteLater()

        self.oldKey = None

    def keyPressEvent(self, event):
        super().keyPressEvent(event)

        # 获取按键数量
        print(event.count())

        # 获取是否是重复事件
        ar = event.isAutoRepeat()
        print(ar)
        if ar:
            return

        # 获取按键代码
        print(event.key())

        # 如果按键匹配标准的按键,返回True
        print(event.matches(QKeySequence.StandardKey.Print))

        # 返回按键上的字符
        name = event.text()
        print(name.lower(), name.upper(), name.capitalize(), name.title(), name.swapcase())

        print("Key Press")



    def keyReleaseEvent(self, event):
        super().keyReleaseEvent(event)

        ar = event.isAutoRepeat()
        print(ar)
        if ar:
            return
        print("Key Release")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QKeyEventInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
