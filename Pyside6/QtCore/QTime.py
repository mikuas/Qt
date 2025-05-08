# coding:utf-8
import random
import sys

from PySide6.QtGui import QFont, Qt, QPainter, QColor, QPalette
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QLayout
from PySide6.QtCore import QTime, QTimer, QPoint

from Interface import WidgetInterface

from FluentWidgets import RoundMenu, Action, TransparentToolButton, FluentIcon, ToggleToolButton, HBoxLayout, setToolTipInfo
from FluentWidgets.components.material import AcrylicMenu


class QTimeInterface(WidgetInterface):
    def __init__(self):
        super().__init__()
        self._pos = self.pos()
        self._isTop = True
        self._isTransparent = True
        self.menu = AcrylicMenu(parent=self)
        self.menu.addAction(Action("随机更改文字颜色", self, triggered=self.toggleTextColor))

        self.button.deleteLater()
        self.infos.deleteLater()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.time = QTime()
        # 设置时间
        self.time.setHMS(1, 1, 1, 1)

        print(self.time.currentTime().toString(Qt.DateFormat.ISODateWithMs))

        self.title = QLabel("QTime", self)
        self.title.setFont(QFont("微软雅黑", 24))
        self.title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        color = QColor('white')
        self.closeButton = TransparentToolButton(FluentIcon.CLOSE.colored(color, color), self)
        self.closeButton.setVisible(False)
        self.closeButton.clicked.connect(self.close)

        self.topButton = TransparentToolButton(FluentIcon.PIN.colored(color, color), self)
        self.topButton.setWindowOpacity(0)
        self.topButton.setVisible(False)
        self.topButton.clicked.connect(lambda: {
            self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
            if self._isTop else self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint),
            self.updateTop(not self._isTop),
            self.show()
        })

        setToolTipInfo(self.closeButton, "关闭窗口", 1000)
        setToolTipInfo(self.topButton, '取消置顶', 1000)

        self.hLayout = HBoxLayout()
        self.hLayout.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.hLayout.addWidget(self.topButton)
        self.hLayout.addWidget(self.closeButton)

        self.box.addLayout(self.hLayout)
        self.box.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: {
            self.title.setText("当前时间: " + self.getTime() + '\n' + self.getH_M_S_MS())
        })
        self.timer.start(1)

        self.palette = QPalette()
        self.palette.setColor(QPalette.ColorRole.WindowText, QColor("deeppink"))
        self.title.setPalette(self.palette)

    def toggleTextColor(self):
        self.palette.setColor(QPalette.ColorRole.WindowText, QColor(self.random, self.random, self.random))
        self.title.setPalette(self.palette)

    def updateTop(self, isTop: bool):
        self._pos = self.pos()
        self._isTop = isTop
        setToolTipInfo(self.topButton, "已置顶" if isTop else "置顶窗口", 1000)

    def show(self):
        self.hide()
        self.move(self._pos)
        super().show()

    @property
    def random(self):
        return random.randint(0, 255)

    def getH_M_S_MS(self):
        time = self.getTime().split(':')
        return f"{time[0]} {time[1]}时/{time[2]}分/{time[3]}秒/{time[4]}毫秒"

    def getTime(self):
        # return self.time.currentTime().toString(Qt.DateFormat.ISODateWithMs)
        """
        h       0~23
        hh      00~23
        H
        HH
        m       0~59
        mm      00~59
        z       0~999
        zzz     000~999
        t       时区 CEST
        ap | a | AP | A     AM/PM
        """
        return self.time.currentTime().toString("A:h:m:s:zzz")

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.dragPos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        print(event.button() == Qt.MouseButton.LeftButton)
        self.move(event.globalPosition().toPoint() - self.dragPos)

    def enterEvent(self, event):
        super().enterEvent(event)
        self._isTransparent = False
        self.closeButton.setVisible(True)
        self.topButton.setVisible(True)
        self.update()

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self._isTransparent = True
        self.closeButton.setVisible(False)
        self.topButton.setVisible(False)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.PenStyle.NoPen)
        if self._isTransparent:
            color = QColor(255, 255, 255, 0)  # 完全透明
        else:
            color = QColor(0, 0, 0, 64)  # 半透明白色
        painter.setBrush(color)
        painter.drawRoundedRect(self.rect(), 8, 8)

    def contextMenuEvent(self, event):
        super().contextMenuEvent(event)
        self.menu.exec(event.globalPos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QTimeInterface()
    window.setContentsMargins(20, 0, 20, 25)
    window.show()
    sys.exit(app.exec())