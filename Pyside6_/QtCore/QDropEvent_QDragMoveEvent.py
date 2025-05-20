# coding:utf-8
import random
import re
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction, QIcon, QDesktopServices, \
    QKeySequence
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar, QSize, QUrl, QRect, QEvent, QEventLoop, \
    QChildEvent, QTimerEvent, QWinEventNotifier, QAbstractNativeEventFilter, QAbstractEventDispatcher, \
    QDynamicPropertyChangeEvent, QMimeData
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar, QToolButton, QStatusBar, QMainWindow, QDockWidget, QDialog, QMdiArea, QMdiSubWindow, QFontDialog, \
    QColorDialog, QFileDialog, QInputDialog, QMessageBox, QErrorMessage, QProgressDialog, QWizard, QWizardPage, QStyle

from Interface import WidgetInterface


class QDropEvent_QDragMoveEvent_Interface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.infos.deleteLater()
        self.button.deleteLater()


        # 接受拖动
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        super().dragEnterEvent(event)
        # 接受事件
        event.accept()

    def dropEvent(self, event):
        super().dropEvent(event)

        # 获取修饰键
        print(event.keyboardModifiers())

        # 获取mime数据
        print(event.mimeData())

        # 获取按下的鼠标按键
        print(event.mouseButtons())

        # 获取释放时的位置
        print(event.pos(), event.posF())

        # 获取采取的动作
        print(event.dropAction())

        # 获取可能实现的动作
        print(event.possibleActions())

        # 系统推荐的动作
        print(event.proposedAction())

        # 接受推荐的动作
        event.acceptProposedAction()

        # 设置释放动作
        event.setDropAction(Qt.DropAction.CopyAction)

        # 获取被拖动对象
        print(event.source())

    def dragMoveEvent(self, event):
        super().dragMoveEvent(event)
        # 在控件或窗口的边界都可以接受移动事件
        event.accept()

        # 指定区域内接受移动事件
        event.accept(QRect(self.rect()))

        # 在整个边界内忽略移动事件
        event.ignore()

        # 在指定区域的内部忽略移动事件
        event.ignore(QRect(self.rect()))

        # 返回可以释放的区域
        print(event.answerRect())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDropEvent_QDragMoveEvent_Interface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
