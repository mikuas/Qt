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
    QDynamicPropertyChangeEvent, QMimeData, QByteArray, QCoreApplication, QLocale, QModelIndex
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget, QMenu, QMenuBar, QWidgetAction, QLineEdit, \
    QToolBar, QToolButton, QStatusBar, QMainWindow, QDockWidget, QDialog, QMdiArea, QMdiSubWindow, QFontDialog, \
    QColorDialog, QFileDialog, QInputDialog, QMessageBox, QErrorMessage, QProgressDialog, QWizard, QWizardPage, QStyle, \
    QListWidget, QListWidgetItem, QStyledItemDelegate, QStyleOptionViewItem, QTableView, QTableWidget, QTableWidgetItem, \
    QTapGesture, QTapAndHoldGesture, QTableWidgetSelectionRange, QStyleOptionTabWidgetFrame, QStyleOptionTab, \
    QStyleOptionTabBarBase, QAbstractItemView, QTreeWidgetItem, QTreeWidget, QTreeView, QTreeWidgetItemIterator
from Interface import WidgetInterface

class TreeStyleDelegate(QStyledItemDelegate):

    def createEditor(self, parent, option, index):
        try:
            from FluentWidgets import LineEdit
            editor = LineEdit(parent)
            editor.setClearButtonEnabled(True)
            return editor
        except ImportError:
            return super().createEditor(parent, option, index)

    def paint(self, painter, option, index):
        # painter.save()
        # painter.setPen(Qt.NoPen)
        # painter.setBrush(QColor('deeppink'))
        # painter.setRenderHints(QPainter.Antialiasing)
        # height = option.rect.height() / 1.5
        # painter.drawRoundedRect(0, height, 5, height, 6, 6)
        # painter.restore()
        super().paint(painter, option, index)
    ...


class TreeWidgetItem(QTreeWidgetItem):
    def __init__(self, *args):
        super().__init__(*args)

        for i in range(self.columnCount()):
            self.setTextAlignment(i, Qt.AlignHCenter | Qt.AlignVCenter)

    # 添加子项
    def addChild(self, child):
        super().addChild(child)
        return self

    # 添加多个子项
    def addChildren(self, children):
        super().addChildren(children)

    # 插入子项
    def insertChild(self, index, child):
        super().insertChild(index, child)

    # 获取子项
    def child(self, index):
        return super().child(index)

    # 获取子项数量
    def childCount(self):
        return super().childCount()

    # 移除子项,移除所有子项
    def takeChild(self, index):
        return super().takeChild(index)
    def takeChildren(self):
        return super().takeChildren()
    def removeChild(self, child):
        super().removeChild(child)

    def setCheckState(self, column, state):
        super().setCheckState(column, state)

    def setChildIndicatorPolicy(self, policy):
        super().setChildIndicatorPolicy(policy)

    # 设置是否激活
    def setDisabled(self, disabled):
        super().setDisabled(disabled)

    # 设置标识
    def setFlags(self, flags):
        super().setFlags(flags)

    # 对子项进行排序
    def sortChildren(self, column, order):
        super().sortChildren(column, order)

    # 获取项的父项
    def parent(self):
        return super().parent()

    # 获取项所在的树结构控件
    def treeWidget(self):
        return super().treeWidget()




class TreeWidget(QTreeWidget):


    def __init__(self, parent=None):
        super().__init__(parent)
        self.__oldColumn = 0
        self.setItemDelegate(TreeStyleDelegate())
        self.setStyleSheet(
            """
            QTreeWidget::item {
                height: 35px;
                outline: none;
            }
            """
        )

        # 设置列
        # self.setColumnCount(10)

        # 设置列宽度
        self.setColumnWidth(1, 100)

        # 设置列是否隐藏
        self.setColumnHidden(1, True)

        # 添加顶层项
        # self.addTopLevelItem()
        items = [[f'root-{i}', 'Tom', str(i), 'Man', "US"] for i in range(1, 101)]
        print(items)
        self.addTopLevelItems([TreeWidgetItem(i) for i in items])

        # 移除顶层项并返回
        # self.takeTopLevelItem()

        # 搜索项,并返回项的列表
        self.findItems('item2', Qt.MatchExactly)

        # 获取项
        for i in range(self.topLevelItemCount()):
            (self.topLevelItem(i).
             addChild(TreeWidgetItem(['sub-root-1', 'Jerry', '20', 'Girl', "US"])
                      .addChild(TreeWidgetItem(['sub-sub-root-1', 'Jerry', '20', 'Girl', "US"])
                                .addChild(TreeWidgetItem(['sub-sub-sub-root-1', 'Jerry', '20', 'Girl', "US"])
                                          .addChild(TreeWidgetItem(['sub-sub-sub-sub-root-1', 'Jerry', '20', 'Girl', "US"])
                                                    )
                                          )
                                )
                      )
             )

        # 设置表头
        self.setHeaderItem(TreeWidgetItem(['Root', 'Name', 'Age', 'Gender', 'City']))

        # 获取不可见的根项
        print(self.invisibleRootItem())

        # 获取指定项之前,之后的项
        print(self.itemAbove(self.topLevelItem(1)))
        print(self.itemBelow(self.topLevelItem(1)))

        # 打开编辑框
        self.doubleClicked.connect(lambda model: {
            self.openPersistentEditor(*self.onItemDoubleClicked(model))
        })

        # 关闭
        self.currentItemChanged.connect(lambda c, p: self.closePersistentEditor(p, self.__oldColumn))

        # 滚动树结构,是指定的项可见
        self.scrollToItem(self.topLevelItem(20))
        self.scrollToItem(self.topLevelItem(0))

        # 获取选中的列表项
        print(self.selectedItems())

        # 只显示指定项的第一列的值
        # self.setFirstColumnSpanned()

        # 在指定项的指定列设置控件
        self.setItemWidget(self.topLevelItem(0), 0, QLabel('Hello World'))

        # 设置选择模式
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # 折叠项,折叠所有项
        self.collapseItem(self.topLevelItem(0))
        self.collapseAll()

        # 展开项,展开所有项
        self.expandItem(self.topLevelItem(0))
        self.expandAll()

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(lambda point: print(self.getItem(point)))

        try:
            from FluentWidgets import SmoothScrollDelegate
            SmoothScrollDelegate(self)
        except ImportError:
            ...

    def getItem(self, point):
        print(point)
        return self.childAt(point)

    def onItemDoubleClicked(self, index: QModelIndex):
        # 获取 item
        item = self.itemFromIndex(index)

        # 获取行列
        row = index.row()
        column = index.column()

        # 获取当前项文本
        text = item.text(column)

        print(f"双击了第{row}行，第{column}列，内容为：{text}")

        self.__oldColumn = column

        return item, column


class QTreeWidget_QTreeWidgetItem_Interface(WidgetInterface):

    def __init__(self):
        super().__init__()
        self.button.deleteLater()
        self.infos.deleteLater()

        self.treeWidget = TreeWidget(self)
        self.box.addWidget(self.treeWidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QTreeWidget_QTreeWidgetItem_Interface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())