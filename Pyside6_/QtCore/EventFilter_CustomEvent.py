# coding:utf-8
import random
import re
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction, QIcon, QDesktopServices, \
    QKeySequence, QDrag, QPixmap, QContextMenuEvent, QChildWindowEvent, QClipboard, QShowEvent, QCloseEvent, QResizeEvent, \
    QMoveEvent, QPaintEvent, QEnterEvent, QFocusEvent, QHideEvent, QWheelEvent
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar, QSize, QUrl, QRect, QEvent, QEventLoop, \
    QChildEvent, QTimerEvent, QWinEventNotifier, QAbstractNativeEventFilter, QAbstractEventDispatcher, \
    QDynamicPropertyChangeEvent, QMimeData, QByteArray, QCoreApplication
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar, QToolButton, QStatusBar, QMainWindow, QDockWidget, QDialog, QMdiArea, QMdiSubWindow, QFontDialog, \
    QColorDialog, QFileDialog, QInputDialog, QMessageBox, QErrorMessage, QProgressDialog, QWizard, QWizardPage, QStyle, \
    QListWidget, QListWidgetItem

from Interface import WidgetInterface


class CustomEvent(QEvent):
    ID = QEvent.registerEventType(2000)

    def __init__(self, position, rect):
        super().__init__(QEvent.Type.User)
        self.__position = position
        self.__rect = rect

    def getPosition(self) -> QPoint:
        return self.__position

    def getRect(self) -> QRect:
        return self.__rect


class EventFilterButton(QPushButton):
    def __init__(self, text='', parent: QWidget = None):
        super().__init__(text, parent)
        parent.installEventFilter(self)

    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.Wheel:
            print(event.angleDelta())

        return super().eventFilter(watched, event)

    def mousePressEvent(self, e):
        super().mousePressEvent(e)
        QCoreApplication.sendEvent(self.window(), CustomEvent(self.pos(), self.rect()))
        QCoreApplication.postEvent(self.window(), CustomEvent(self.pos(), self.rect()))


class EventFilter_CustomEvent_Interface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.button = EventFilterButton("Filter", self)
        self.box.addWidget(self.button)

    def customEvent(self, event: CustomEvent):
        if event.type() == QEvent.Type.User:
            print(event.getPosition(), event.getRect())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EventFilter_CustomEvent_Interface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())