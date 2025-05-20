# coding:utf-8
import random
import re
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction, QIcon, QDesktopServices, \
    QKeySequence, QDrag, QPixmap, QContextMenuEvent, QChildWindowEvent, QClipboard, QShowEvent, QCloseEvent, QResizeEvent, \
    QMoveEvent, QPaintEvent, QEnterEvent, QFocusEvent, QHideEvent, QWheelEvent
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar, QSize, QUrl, QRect, QEvent, QEventLoop, \
    QChildEvent, QTimerEvent, QWinEventNotifier, QAbstractNativeEventFilter, QAbstractEventDispatcher, \
    QDynamicPropertyChangeEvent, QMimeData, QByteArray
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar, QToolButton, QStatusBar, QMainWindow, QDockWidget, QDialog, QMdiArea, QMdiSubWindow, QFontDialog, \
    QColorDialog, QFileDialog, QInputDialog, QMessageBox, QErrorMessage, QProgressDialog, QWizard, QWizardPage, QStyle

from Interface import WidgetInterface


class QTimerEventInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.startTimer(1000, Qt.TimerType.CoarseTimer)
        self.startTimer(2000, Qt.TimerType.VeryCoarseTimer)
        self.startTimer(3000, Qt.TimerType.PreciseTimer)

    def timerEvent(self, event):
        super().timerEvent(event)

        # id
        ID = event.timerId()
        print(ID)

        if ID == 2:
            self.killTimer(ID)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QTimerEventInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())