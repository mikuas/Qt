# coding:utf-8
import random
import re
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction, QIcon, QDesktopServices, \
    QKeySequence, QDrag, QPixmap, QContextMenuEvent, QChildWindowEvent, QClipboard, QShowEvent, QCloseEvent, \
    QResizeEvent, \
    QMoveEvent, QPaintEvent, QEnterEvent, QFocusEvent, QHideEvent, QWheelEvent, QBrush, QPen
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar, QSize, QUrl, QRect, QEvent, QEventLoop, \
    QChildEvent, QTimerEvent, QWinEventNotifier, QAbstractNativeEventFilter, QAbstractEventDispatcher, \
    QDynamicPropertyChangeEvent, QMimeData, QByteArray, QCoreApplication
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar, QToolButton, QStatusBar, QMainWindow, QDockWidget, QDialog, QMdiArea, QMdiSubWindow, QFontDialog, \
    QColorDialog, QFileDialog, QInputDialog, QMessageBox, QErrorMessage, QProgressDialog, QWizard, QWizardPage, QStyle, \
    QListWidget, QListWidgetItem, QStyledItemDelegate, QStyleOptionViewItem, QTableView, QTableWidget, QTableWidgetItem, \
    QTapGesture, QTapAndHoldGesture, QTableWidgetSelectionRange, QStyleOptionTabWidgetFrame, QStyleOptionTab, QStyleOptionTabBarBase
from Interface import WidgetInterface


class TableWidgetItem(QTableWidgetItem): ...



class TableWidget(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置行数
        self.setRowCount(10)

        # 设置列数
        self.setColumnCount(5)

        # 获取行数,列数
        print(self.rowCount(), self.columnCount())

        # 在指定行,列设定表格项
        self.setItem(0, 0, TableWidgetItem("Hello World"))

        # 移除并返回表格项
        print(self.takeItem(0, 0))

        # 设置当前表格项
        # self.setCurrentItem()

        # 获取当前行,列
        print(self.currentRow(), self.currentColumn())

        # 设置水平,垂直表头
        # self.setHorizontalHeaderItem(), self.setVerticalHeaderItem()
        self.setHorizontalHeaderLabels(["A", "B", "C", "D", "E"])
        self.setVerticalHeaderLabels(["A", "B", "C", "D", "E"])

        # print(self.takeVerticalHeaderItem())


class QTableWidget_QTableWidgetItem_Interface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()
        self.tableWidget = TableWidget(self)

        self.box.addWidget(self.tableWidget)

        try:
            from FluentWidgets import TableWidget as tw
            t = tw(self)
            t.setRowCount(10)
            t.setColumnCount(5)
            self.box.addWidget(t)
        except ImportError:
            ...



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QTableWidget_QTableWidgetItem_Interface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())