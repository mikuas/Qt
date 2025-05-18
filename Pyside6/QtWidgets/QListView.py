# coding:utf-8

import sys
from PySide6.QtWidgets import QApplication, QWidget, QListView, QHBoxLayout, QStyledItemDelegate, \
    QStyle
from PySide6.QtCore import Qt, QStringListModel, QSize
from PySide6.QtGui import Qt, QColor, QPen, QPainter, QFont


class RoundListWidgetItemDelegate(QStyledItemDelegate):
    def __init__(self, isFull=False, parent=None):
        super().__init__(parent)
        self.__isFull = isFull
        self.__color = None         # type: QColor
        self.__textColor = None     # type: QColor

    def setIsFull(self, isFull: bool):
        self.__isFull = isFull

    def setColor(self, color: str | QColor):
        self.__color = QColor(color)

    def setTextColor(self, textColor: str | QColor):
        self.__textColor = QColor(textColor)

    def paint(self, painter, option, index):
        painter.save()

        # 设置背景
        rect = option.rect.adjusted(2, 2, -2, -2)
        isDark = False
        textColor = self.__textColor or (QColor("#000000") if isDark else QColor("#ffffff"))
        if option.state & (QStyle.StateFlag.State_Selected | QStyle.StateFlag.State_MouseOver):
            color = self.__color or QColor('deeppink') # or themeColor()
        else:
            color = QColor("#000000") if isDark else QColor("#E8E8E8")
            textColor = self.__textColor or (QColor("#ffffff") if isDark else QColor("#000000"))
        painter.setRenderHint(QPainter.RenderHint.Antialiasing | QPainter.RenderHint.TextAntialiasing)
        if self.__isFull:
            painter.setPen(Qt.NoPen)
            painter.setBrush(color)
        else:
            pen = QPen(color)
            pen.setWidth(2)
            painter.setPen(pen)
            textColor = self.__textColor or (QColor("#ffffff") if isDark else QColor("#000000"))
        painter.drawRoundedRect(rect, 8, 8)

        # 设置字体
        alignment = index.data(Qt.ItemDataRole.TextAlignmentRole) or Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        text = index.data()
        painter.setPen(textColor)
        painter.setFont(QFont("微软雅黑", 12))
        painter.drawText(rect.adjusted(10, 0, -10, 0), alignment, text)

        painter.restore()

    def sizeHint(self, option, index):
        # 设置每一项的高度为35像素，宽度自适应
        return QSize(option.rect.width(), 50)
        

class ListView(QListView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setItemDelegate(RoundListWidgetItemDelegate(parent=self))
        
        self.stringListModel = QStringListModel(self)
        self.stringListModel.setStringList(
            [f"Item {_}" for _ in range(1, 1001)]
        )
        
        # 设置模型
        self.setModel(self.stringListModel)
        
        try:
            from FluentWidgets import SmoothScrollDelegate
            self.scrollDelegate = SmoothScrollDelegate(self)
        except ImportError:
            ...
        
        
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.box = QHBoxLayout(self)
        self.listView = ListView(self)
        
        self.box.addWidget(self.listView)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())