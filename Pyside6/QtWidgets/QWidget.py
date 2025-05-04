# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette, QTextCharFormat, QAction
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout, QCalendarWidget, QLCDNumber, QDateTimeEdit, \
    QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout, QGridLayout, QSplitter, QGroupBox, QFrame, QScrollArea, \
    QScrollBar, QTabWidget, QTabBar, QPushButton, QStackedWidget
from PySide6.QtCore import QTime, QTimer, QPoint, QDateTime, QDate, QCalendar


class QWidgetInterface(QWidget):
    def __init__(self):
        super().__init__()
        from qframelesswindow import WindowEffect, StandardTitleBar
        self.ef = WindowEffect(self)
        self.box = QVBoxLayout(self)
        self.setContentsMargins(0, 0, 0, 0)
        self.box.setContentsMargins(0, 0, 0, 0)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ef.setMicaEffect(self.winId(), isAlt=True)

        # self.s = StandardTitleBar(self)
        # self.s.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        # self.s.raise_()

        # 提升控件, 使控件显示在窗口最上层
        self.raise_()

        # 降低控件, 使控件显示在窗口最下层
        self.lower()

        # 设置窗口不透明度
        self.setWindowOpacity(1)

        # 获取窗口类型
        print(self.windowType())

        # 获取窗口状态
        print(self.windowState())

        # 设置成活动窗口,活动窗口可以获得键盘输入
        self.isActiveWindow()

        # 全屏显示
        # self.showFullScreen()

        # 设置是否可以对窗口进行刷新
        self.setUpdatesEnabled(True)

        # 刷新窗口
        self.update()

        # 设置右键快捷键弹出策略
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)

        # 添加动作
        self.addAction(QAction('Hello', self))

        # 设置失效状态
        self.setDisabled(False)

        # 设置是否激活
        self.setEnabled(False)

        # 获取是否是独立窗口
        print(self.isWindow())

        # 获取指定位置处的控件
        # self.childAt()

        # 设置获得焦点
        self.setFocus()

        # 设置是否接受鼠标的拖放
        self.setAcceptDrops(True)

        # 设置是否跟踪鼠标移动事件
        self.setMouseTracking(True)

        # 获取所有键盘输入事件, 其他控件不在接受键盘输入事件
        self.grabKeyboard()

        # 设置tab键顺序
        # self.setTabOrder()

        # 设置窗口模式
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        """
            Qt.NonModal	非模态窗口（默认），不会阻止与其他窗口交互。
            Qt.WindowModal	阻止与其父窗口交互，但不影响应用程序中的其他窗口。
            Qt.ApplicationModal	阻止与整个应用程序的所有窗口交互，直到该窗口关闭。   
        """


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidgetInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
