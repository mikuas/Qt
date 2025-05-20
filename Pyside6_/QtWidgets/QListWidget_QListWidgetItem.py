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
    QListWidget, QListWidgetItem, QStyledItemDelegate, QStyleOptionViewItem

from Interface import WidgetInterface


class CustomDelegate(QStyledItemDelegate):

    def paint(self, painter, option, index):
        painter.save()

        # 设置背景
        rect = option.rect.adjusted(2, 2, -2, -2)
        if option.state & QStyle.StateFlag.State_Selected:
            color = QColor("deeppink")
        elif option.state & QStyle.StateFlag.State_MouseOver:
            color = QColor("pink")
        else:
            color = QColor("#ffffff")
        # painter.setPen(Qt.NoPen)
        # painter.setBrush(color)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing | QPainter.RenderHint.TextAntialiasing |
                              QPainter.RenderHint.SmoothPixmapTransform | QPainter.RenderHint.LosslessImageRendering)
        pen = QPen(color)
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawRoundedRect(rect, 8, 8)

        # 设置字体
        text = index.data()
        painter.setPen(QColor("#333"))
        painter.setFont(QFont("Arial", 12))
        painter.drawText(rect.adjusted(10, 0, 0, 0), index.data(Qt.ItemDataRole.TextAlignmentRole) or Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter, text)

        painter.restore()


class CustomListWidgetItem(QListWidgetItem):
    def __init__(self, text):
        super().__init__(text)
        self.setSizeHint(QSize(0, 50))

        # 设置勾选状态
        self.setCheckState(Qt.CheckState.Checked)

        # self.setFlags(Qt.ItemFlag.ItemIsDragEnabled)
        # self.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsDragEnabled | Qt.ItemFlag.ItemIsEnabled
        #               | Qt.ItemFlag.ItemIsDropEnabled)

        print(self.flags())

        # 设置可拖拽
        self.setFlags(self.flags() | Qt.ItemFlag.ItemIsDragEnabled)


class QListWidget_QListWidgetItem_Interface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.setStyleSheet(
            """
            QListWidget {
            background: transparent;
            border: none;
            padding: 0;
            margin: 0;
            }
            """
        )


        self.listWidget = QListWidget(self)
        self.box.addWidget(self.listWidget)
        # self.listWidget.setItemDelegate(CustomDelegate())

        # 设置拖动模式
        self.listWidget.setDragDropMode(QListWidget.DragDropMode.InternalMove)

        self.items = [f'item{_}' for _ in range(1, 101)]
        self.items.reverse()
        # 添加项
        # self.listWidget.addItem()

        for item in self.items:
            self.listWidget.addItem(CustomListWidgetItem(item))


        self.listWidget.currentItemChanged.connect(lambda item: print(item.text()))

        # 打开指定项的编辑框,并返回该项
        self.listWidget.openPersistentEditor(self.listWidget.item(1))
        self.listWidget.closePersistentEditor(self.listWidget.item(1))

        # 滚动到指定的项
        self.listWidget.scrollToItem(self.listWidget.item(10))

        # 设置是否可以进行排序
        self.listWidget.setSortingEnabled(True)

        # 按照排序方式进行项的排序
        self.listWidget.sortItems(Qt.SortOrder.AscendingOrder)

        print(self.listWidget.supportedDropActions())

        self.listWidget.setAcceptDrops(True)
        # 设置交替色
        self.listWidget.setAlternatingRowColors(True)

        # 清除选择
        self.listWidget.clearSelection()


    def dragEnterEvent(self, event):
        super().dragEnterEvent(event)
        event.accept()

    def dropEvent(self, event):
        super().dropEvent(event)
        event.accept()

    def dragMoveEvent(self, event):
        super().dragMoveEvent(event)
        print(event.pos())


    def mouseDoubleClickEvent(self, event):
        super().mouseDoubleClickEvent(event)
        print(True)
        self.listWidget.openPersistentEditor(self.listWidget.item(self.listWidget.currentRow()))


    def contextMenuEvent(self, event):
        super().contextMenuEvent(event)
        item = self.childAt(event.pos())
        print(item, type(item), item is self.listWidget.item(0))
        # print(item, isinstance(item, QListWidgetItem))
        # self.listWidget.openPersistentEditor(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QListWidget_QListWidgetItem_Interface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())