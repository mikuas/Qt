# coding:utf-8
import random
import re
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction, QIcon, QDesktopServices
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar, QSize, QUrl, QRect
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar, QToolButton, QStatusBar, QMainWindow, QDockWidget, QDialog, QMdiArea, QMdiSubWindow, QFontDialog, \
    QColorDialog, QFileDialog, QInputDialog

from Interface import WidgetInterface


class QInputDialogInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.infos.deleteLater()

        self.dialog = QInputDialog(self)
        self.box.addWidget(self.button)
        self.button.clicked.connect(self.dialog.show)

        # 设置输入对话框的类型
        self.dialog.setInputMode(QInputDialog.InputMode.TextInput)

        # 设置输入对话框的参数
        self.dialog.setOption(QInputDialog.InputDialogOption.UseListViewForComboBoxItems, True)

        # 设置对话框标签名称
        self.dialog.setLabelText('Hello World')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QInputDialogInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
