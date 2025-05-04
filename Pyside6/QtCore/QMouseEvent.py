# coding:utf-8
import random
import re
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction, QIcon, QDesktopServices
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar, QSize, QUrl, QRect, QEvent, QEventLoop, \
    QChildEvent, QTimerEvent, QWinEventNotifier, QAbstractNativeEventFilter, QAbstractEventDispatcher, \
    QDynamicPropertyChangeEvent
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar, QToolButton, QStatusBar, QMainWindow, QDockWidget, QDialog, QMdiArea, QMdiSubWindow, QFontDialog, \
    QColorDialog, QFileDialog, QInputDialog, QMessageBox, QErrorMessage, QProgressDialog, QWizard, QWizardPage, QStyle

from Interface import WidgetInterface


class QMouseEventInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.infos.deleteLater()
        self.button.deleteLater()


    def mouseDoubleClickEvent(self, event):
        super().mouseDoubleClickEvent(event)


    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        print(event.button(), end='\n\n')
        print(event.buttons(), end='\n\n')
        print(event.flags(), end='\n\n')
        print(event.modifiers(), end='\n\n')

        print(event.globalPosition().toPoint(), end=' Global QPoint \n\n')
        print(event.globalPosition().toPoint().x(), end=' Global X \n\n')
        print(event.globalPosition().toPoint().y(), end=' Global Y \n\n')

        print(event.localPos(), end=' 局部鼠标位置 \n\n')
        print(event.screenPos(), end=' 屏幕鼠标位置 \n\n')






    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMouseEventInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
