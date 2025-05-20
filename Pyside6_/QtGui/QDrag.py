# coding:utf-8
import random
import re
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction, QIcon, QDesktopServices, \
    QKeySequence, QDrag, QPixmap, QContextMenuEvent
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar, QSize, QUrl, QRect, QEvent, QEventLoop, \
    QChildEvent, QTimerEvent, QWinEventNotifier, QAbstractNativeEventFilter, QAbstractEventDispatcher, \
    QDynamicPropertyChangeEvent, QMimeData, QByteArray
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar, QToolButton, QStatusBar, QMainWindow, QDockWidget, QDialog, QMdiArea, QMdiSubWindow, QFontDialog, \
    QColorDialog, QFileDialog, QInputDialog, QMessageBox, QErrorMessage, QProgressDialog, QWizard, QWizardPage, QStyle

from Interface import WidgetInterface


class DragLabel(QLabel):
    def __init__(self, text='', parent=None):
        super().__init__(text, parent)
        self.setFixedSize(200, 35)

    def mousePressEvent(self, event):
        super().mouseMoveEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mimeData = QMimeData()
            mimeData.setText('Hello World')
            drag.setMimeData(mimeData)

            # 设置拖拽时的光标形状
            # drag.setDragCursor()

            drag.setPixmap(QPixmap(r"C:\Users\Administrator\OneDrive\Pictures\微信图片_20250501162521.jpg"))

            # 开始拖动操作, 并返回释放时的动作7
            drag.exec(Qt.DropAction.CopyAction)

            # 返回默认的释放动作
            print(drag.defaultAction())

class QDragInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.infos.deleteLater()
        self.button.deleteLater()

        class Button(QPushButton):
            def __init__(self, parent=None):
                super().__init__(parent)

            def mousePressEvent(self, e):
                super().mousePressEvent(e)
                if e.button() == Qt.MouseButton.LeftButton:
                    self.drag = QDrag(self)
                    self.drag.setHotSpot(e.position().toPoint())
                    mineData = QMimeData()
                    self.drag.setMimeData(mineData)
                    self.drag.exec()

        self.box.addWidget(DragLabel("Hello World"))

        self.button = Button(self)
        self.button.move(100, 100)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        super().dragEnterEvent(event)
        self.child = self.childAt(event.position().toPoint())
        print("ENTER")
        event.accept()

    def dragMoveEvent(self, event):
        if self.child:
            print("MOVE")
            self.child.move(event.position().toPoint())

    def dropEvent(self, event):
        super().dropEvent(event)
        if self.child:
            self.child.move(event.position().toPoint())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDragInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
