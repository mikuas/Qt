# coding:utf-8
import random
import re
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction, QIcon, QDesktopServices, \
    QKeySequence, QDrag, QPixmap, QContextMenuEvent, QChildWindowEvent, QClipboard, QShowEvent, QCloseEvent, \
    QResizeEvent, \
    QMoveEvent, QPaintEvent, QEnterEvent, QFocusEvent, QHideEvent, QWheelEvent, QBrush, QPen, QStandardItemModel
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar, QSize, QUrl, QRect, QEvent, QEventLoop, \
    QChildEvent, QTimerEvent, QWinEventNotifier, QAbstractNativeEventFilter, QAbstractEventDispatcher, \
    QDynamicPropertyChangeEvent, QMimeData, QByteArray, QCoreApplication, QLocale
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar, QToolButton, QStatusBar, QMainWindow, QDockWidget, QDialog, QMdiArea, QMdiSubWindow, QFontDialog, \
    QColorDialog, QFileDialog, QInputDialog, QMessageBox, QErrorMessage, QProgressDialog, QWizard, QWizardPage, QStyle, \
    QListWidget, QListWidgetItem, QStyledItemDelegate, QStyleOptionViewItem, QTableView, QTableWidget, QTableWidgetItem, \
    QTapGesture, QTapAndHoldGesture, QTableWidgetSelectionRange, QStyleOptionTabWidgetFrame, QStyleOptionTab, \
    QStyleOptionTabBarBase, QAbstractItemView
from Interface import WidgetInterface

count = 0


class CustomDelegate(QStyledItemDelegate):

    def createEditor(self, parent, option, index):
        try:
            from FluentWidgets import LineEdit
            editor = LineEdit(parent)
            editor.setClearButtonEnabled(True)
            editor.setFixedHeight(option.rect.height())
            return editor
        except ImportError:
            return super().createEditor(parent, option, index)

    def setEditorData(self, editor, index):
        editor.setText(index.model().data(index, Qt.EditRole))

    def setModelData(self, editor, model, index):
        model.setData(index, editor.text(), Qt.EditRole)

    def paint(self, painter, option, index):
        painter.save()
        painter.setClipping(True)
        global count
        count += 1

        # 前,背景色
        color = index.data(Qt.ItemDataRole.ForegroundRole)
        bgcColor = index.data(Qt.ItemDataRole.BackgroundRole)

        # 复选框状态
        checkState = index.data(Qt.ItemDataRole.CheckStateRole)

        print(color, bgcColor, checkState)

        # 设置背景颜色（比如悬停或选中时）
        if option.state & QStyle.StateFlag.State_Selected:
            painter.fillRect(option.rect, QColor("#cceeff"))
        elif option.state & QStyle.StateFlag.State_MouseOver:
            painter.fillRect(option.rect, QColor("#e0f7fa"))
        else:
            painter.fillRect(option.rect, QColor('#ffffff'))

        # 获取图标
        print(f"Left: {option.rect.left()}")
        icon = index.data(Qt.ItemDataRole.DecorationRole)  # 获取图标
        icon.paint(painter, option.rect)  # 绘制图标

        # 设置字体颜色和大小
        text = index.data(Qt.ItemDataRole.DisplayRole)
        alignment = index.model().data(index, Qt.ItemDataRole.TextAlignmentRole)
        print(f'alignment: {alignment}')
        painter.setPen(QColor("#333333"))
        painter.setFont(QFont("微软雅黑", 10))
        painter.drawText(option.rect.adjusted(5, 0, -5, 0), alignment, text)

        painter.restore()

        print(count)


class TableWidgetItem(QTableWidgetItem): ...


class TableWidget(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.__items = []

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

        row = 1_0_0_0
        colum = 2_4
        self.setRowCount(row)
        self.setColumnCount(colum)

        icon = QIcon(r"C:\Users\Administrator\OneDrive\Pictures\ff.jpg")

        for i in range(row):
            for j in range(colum):
                item = TableWidgetItem(f"{i + 1}_{j + 1}")
                self.__items.append(item)
                item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
                item.setIcon(icon)
                self.setItem(i, j, item)


        # 获取满足条件的表格项和列
        print(self.findItems("Hello World", Qt.MatchFlag.MatchExactly))
        print(self.findItems("Hello", Qt.MatchFlag.MatchExactly))

        print(len(self.items()))

        lenght = 0
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                self.item(i, j)
                lenght += 1
        print(lenght)

        # self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

    def items(self):
        return self.__items

    def setItemSize(self, width: int, height: int):
        for item in self.items():
            item.setSizeHint(QSize(width, height))


class QTableWidget_QTableWidgetItem_Interface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()
        self.tableWidget = TableWidget(self)

        self.tableWidget.setItemDelegate(CustomDelegate(self))
        # self.tableWidget.setItemSize(50, 35)

        self.box.addWidget(self.tableWidget)

        try:
            from FluentWidgets import TableWidget as tw, SmoothScrollDelegate, TableView
            t = tw(self)
            row = 1_0_0_0
            colum = 2_4
            t.setRowCount(row)
            t.setColumnCount(colum)

            for i in range(row):
                for j in range(colum):
                    item = TableWidgetItem(f"{i + 1}_{j + 1}")
                    item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
                    t.setItem(i, j, item)

            SmoothScrollDelegate(self.tableWidget)
            self.box.addWidget(t)
            ...
        except ImportError:
            ...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QTableWidget_QTableWidgetItem_Interface()
    window.resize(800, 520)
    window.show()
    try:
        from FluentWidgets import FluentTranslator, ListWidget, ListView

        # app.installTranslator(FluentTranslator(QLocale(QLocale.Language.Chinese, QLocale.Country.China), window))
        app.installTranslator(FluentTranslator(QLocale(), window))

        from qframelesswindow import WindowEffect
        #
        # window.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        # window.setStyleSheet('background: transparent;')
        #
        # we = WindowEffect(window)
        # we.setMicaEffect(window.winId(), isAlt=True)

    except ImportError:
        ...
    sys.exit(app.exec())