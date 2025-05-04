# coding:utf-8
import random
import re
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction, QIcon, QDesktopServices, \
    QKeySequence, QDrag, QPixmap, QContextMenuEvent, QChildWindowEvent, QClipboard
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar, QSize, QUrl, QRect, QEvent, QEventLoop, \
    QChildEvent, QTimerEvent, QWinEventNotifier, QAbstractNativeEventFilter, QAbstractEventDispatcher, \
    QDynamicPropertyChangeEvent, QMimeData, QByteArray
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar, QToolButton, QStatusBar, QMainWindow, QDockWidget, QDialog, QMdiArea, QMdiSubWindow, QFontDialog, \
    QColorDialog, QFileDialog, QInputDialog, QMessageBox, QErrorMessage, QProgressDialog, QWizard, QWizardPage, QStyle

from Interface import WidgetInterface


class QContextMenuEventInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.infos.deleteLater()
        self.button.deleteLater()

    def contextMenuEvent(self, event):
        super().contextMenuEvent(event)

        # 全局坐标点
        globalPos = event.globalPos()
        print("全局坐标点:", globalPos, "X:", globalPos.x(), "Y:", globalPos.y())

        # 局部坐标点
        pos = event.pos()
        print("局部坐标点:", pos, "X:", pos.x(), "Y:", pos.y())

        # 产生上下文菜单的原因
        print(event.reason())

        # 获取修饰键
        print(event.modifiers())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QContextMenuEventInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
