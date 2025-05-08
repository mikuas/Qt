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


class CustomDelegate(QStyledItemDelegate):

    def createEditor(self, parent, option, index):
        try:
            from FluentWidgets import LineEdit
            return LineEdit(parent)
        except ImportError:
            return super().createEditor(parent, option, index)

    def setEditorData(self, editor, index):
        editor.setText(index.model().data(index, Qt.EditRole))

    def setModelData(self, editor, model, index):
        model.setData(index, editor.text(), Qt.EditRole)

    def paint(self, painter, option, index):
        painter.save()

        # 设置背景颜色（比如悬停或选中时）
        if option.state & QStyle.StateFlag.State_Selected:
            painter.fillRect(option.rect, QColor("#cceeff"))
        elif option.state & QStyle.StateFlag.State_MouseOver:
            painter.fillRect(option.rect, QColor("#e0f7fa"))
        else:
            painter.fillRect(option.rect, QColor("#ffffff"))

        # 设置字体颜色和大小
        text = index.data()
        painter.setPen(QColor("#333333"))
        painter.setFont(QFont("微软雅黑", 10))
        painter.drawText(option.rect.adjusted(5, 0, -5, 0), Qt.AlignLeft | Qt.AlignVCenter, text)

        painter.restore()


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

        # 清空表格项和表头的内容
        self.clear()
        # 清空表格项的内容
        self.clearContents()

        self.setItem(0, 0, TableWidgetItem("Hello"))
        self.setItem(0, 1, TableWidgetItem("Hello World"))

        self.item(0, 1).setTextAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        # 获取满足条件的表格项和列
        print(self.findItems("Hello World", Qt.MatchFlag.MatchExactly))
        print(self.findItems("Hello", Qt.MatchFlag.MatchExactly))


class QTableWidget_QTableWidgetItem_Interface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()
        self.tableWidget = TableWidget(self)

        self.tableWidget.setItemDelegate(CustomDelegate(self))

        self.box.addWidget(self.tableWidget, 1)

        try:
            from FluentWidgets import TableWidget as tw, SmoothScrollDelegate
            t = tw(self)
            t.setRowCount(10)
            t.setColumnCount(5)
            self.box.addWidget(t)

            SmoothScrollDelegate(self.tableWidget)
        except ImportError:
            ...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QTableWidget_QTableWidgetItem_Interface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())