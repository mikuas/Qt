# coding:utf-8
import random
import re
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction, QIcon, QDesktopServices, \
    QKeySequence, QDrag, QPixmap, QContextMenuEvent, QChildWindowEvent, QClipboard, QShowEvent, QCloseEvent, QResizeEvent, \
    QMoveEvent, QPaintEvent, QEnterEvent, QFocusEvent, QHideEvent
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar, QSize, QUrl, QRect, QEvent, QEventLoop, \
    QChildEvent, QTimerEvent, QWinEventNotifier, QAbstractNativeEventFilter, QAbstractEventDispatcher, \
    QDynamicPropertyChangeEvent, QMimeData, QByteArray
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar, QToolButton, QStatusBar, QMainWindow, QDockWidget, QDialog, QMdiArea, QMdiSubWindow, QFontDialog, \
    QColorDialog, QFileDialog, QInputDialog, QMessageBox, QErrorMessage, QProgressDialog, QWizard, QWizardPage, QStyle

from Interface import WidgetInterface


class QClipboardInterface(WidgetInterface):
    def __init__(self):
        super().__init__(enit=True)
        self.infos.deleteLater()

        self.clipboard = QClipboard(self)
        self.edit.setPlaceholderText("设置剪贴板内容")
        self.button.setText("确定")

        # 将文本复制到剪贴板
        self.clipboard.setText("Ciallo～(∠・ω< )⌒☆")

        # 从剪贴板上获取文本
        print(self.clipboard.text())

        # 将QPixmap图像复制到剪贴板上
        # self.clipboard.setPixmap(QPixmap())

        # 将QImage图像复制到剪贴板上
        # self.clipboard.setImage(QImage())

        # 将QMimeData数据赋值到剪贴板上
        self.clipboard.setMimeData(QMimeData())

        # 清空剪贴板
        self.clipboard.clear()

        self.box.addWidget(self.edit)
        self.box.addWidget(self.button)

        self.button.clicked.connect(lambda: {
            self.clipboard.setText(self.edit.text())
        })

        self.clipboard.changed.connect(lambda: print('change'))
        self.clipboard.dataChanged.connect(lambda: print("data change"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QClipboardInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
