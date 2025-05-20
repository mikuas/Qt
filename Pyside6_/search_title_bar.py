# coding:utf-8
import sys

from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QIcon, QPainter, QColor
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication

from FluentWidgets import LineEdit
from qfluentwidgets import FluentWindow

from qfluentwidgets.components.widgets.frameless_window import FramelessWindow
from qframelesswindow import TitleBarButton
from qframelesswindow.titlebar import MinimizeButton, CloseButton, MaximizeButton
from qframelesswindow.utils import startSystemMove, toggleMaxState


class TitleBarBase(QWidget):
    """ Title bar base class """

    def __init__(self, parent):
        super().__init__(parent)
        self.minBtn = MinimizeButton(parent=self)
        self.closeBtn = CloseButton(parent=self)
        self.maxBtn = MaximizeButton(parent=self)

        self._isDoubleClickEnabled = True

        self.resize(200, 32)
        self.setFixedHeight(32)

        # connect signal to slot
        self.minBtn.clicked.connect(self.window().showMinimized)
        self.maxBtn.clicked.connect(self.__toggleMaxState)
        self.closeBtn.clicked.connect(self.window().close)

        self.window().installEventFilter(self)

    def eventFilter(self, obj, e):
        if obj is self.window():
            if e.type() == QEvent.WindowStateChange:
                self.maxBtn.setMaxState(self.window().isMaximized())
                return False

        return super().eventFilter(obj, e)

    def mouseDoubleClickEvent(self, event):
        """ Toggles the maximization state of the window """
        if event.button() != Qt.LeftButton or not self._isDoubleClickEnabled:
            return

        self.__toggleMaxState()

    def mouseMoveEvent(self, e):
        if sys.platform != "win32" or not self.canDrag(e.pos()):
            return

        startSystemMove(self.window(), e.globalPos())

    def mousePressEvent(self, e):
        if sys.platform == "win32" or not self.canDrag(e.pos()):
            return

        startSystemMove(self.window(), e.globalPos())

    def __toggleMaxState(self):
        """ Toggles the maximization state of the window and change icon """
        toggleMaxState(self.window())

    def _isDragRegion(self, pos):
        """ Check whether the position belongs to the area where dragging is allowed """
        width = 0
        for button in self.findChildren(TitleBarButton):
            if button.isVisible():
                width += button.width()

        return 0 < pos.x() < self.width() - width

    def _hasButtonPressed(self):
        """ whether any button is pressed """
        return any(btn.isPressed() for btn in self.findChildren(TitleBarButton))

    def canDrag(self, pos):
        """ whether the position is draggable """
        return self._isDragRegion(pos) and not self._hasButtonPressed()

    def setDoubleClickEnabled(self, isEnabled):
        """ whether to switch window maximization status when double clicked
        Parameters
        ----------
        isEnabled: bool
            whether to enable double click
        """
        self._isDoubleClickEnabled = isEnabled



class TitleBar(TitleBarBase):
    """ Title bar """

    def __init__(self, parent):
        super().__init__(parent)
        self.hBoxLayout = QHBoxLayout(self)

        # add buttons to layout
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.addStretch(1)
        self.hBoxLayout.addWidget(self.minBtn, 0, Qt.AlignRight)
        self.hBoxLayout.addWidget(self.maxBtn, 0, Qt.AlignRight)
        self.hBoxLayout.addWidget(self.closeBtn, 0, Qt.AlignRight)


class StandardTitleBar(TitleBar):
    """ Title bar with icon and title """

    def __init__(self, parent):
        super().__init__(parent)
        # add window icon
        self.iconLabel = QLabel(self)
        self.iconLabel.setFixedSize(20, 20)
        self.hBoxLayout.insertSpacing(0, 10)
        self.hBoxLayout.insertWidget(1, self.iconLabel, 0, Qt.AlignLeft)
        self.window().windowIconChanged.connect(self.setIcon)

        # add title label
        self.titleLabel = QLabel(self)
        self.hBoxLayout.insertWidget(2, self.titleLabel, 0, Qt.AlignLeft)
        self.titleLabel.setStyleSheet("""
            QLabel{
                background: transparent;
                font: 13px 'Segoe UI';
                padding: 0 4px
            }
        """)
        self.window().windowTitleChanged.connect(self.setTitle)

    def setTitle(self, title):
        """ set the title of title bar
        Parameters
        ----------
        title: str
            the title of title bar
        """
        self.titleLabel.setText(title)
        self.titleLabel.adjustSize()

    def setIcon(self, icon):
        """ set the icon of title bar
        Parameters
        ----------
        icon: QIcon | QPixmap | str
            the icon of title bar
        """
        self.iconLabel.setPixmap(QIcon(icon).pixmap(20, 20))


class SearchTitleBar(StandardTitleBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.window().installEventFilter(self)
        self.setFixedHeight(45)

        self.hBoxLayout.removeWidget(self.minBtn)
        self.hBoxLayout.removeWidget(self.maxBtn)
        self.hBoxLayout.removeWidget(self.closeBtn)

        self.searchBox = LineEdit(self)
        self.hBoxLayout.addWidget(self.searchBox, 1, Qt.AlignHCenter | Qt.AlignBottom)
        self.hBoxLayout.addStretch(1)

        self.hBoxLayout.addWidget(self.minBtn, 0, Qt.AlignTop | Qt.AlignRight)
        self.hBoxLayout.addWidget(self.maxBtn, 0, Qt.AlignTop | Qt.AlignRight)
        self.hBoxLayout.addWidget(self.closeBtn, 0, Qt.AlignTop | Qt.AlignRight)

        self.raise_()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.searchBox.setFixedWidth(self.width() / 3)


class Window(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.setTitleBar(SearchTitleBar(self))
        self.setWindowTitle('hello world')
        self.setWindowIcon(QIcon(r"C:\Users\Administrator\OneDrive\Pictures\ff.jpg"))

        self.setContentsMargins(0, 58, 0, 0)

        # if isinstance(self, FluentWindow):
        #     self.navigationInterface.displayModeChanged.connect(self.titleBar.raise_)
        #     return

        class W(QWidget):
            def __init__(self, parent):
                super().__init__(parent)

            def paintEvent(self, event):
                painter = QPainter(self)
                painter.setRenderHint(QPainter.Antialiasing)
                painter.setPen(Qt.NoPen)
                painter.setBrush(QColor('skyblue'))
                painter.drawRect(self.rect())

        self.box = QHBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.box.addWidget(W(self))



if __name__ == '__main__':

    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    window = Window()
    window.windowEffect.addWindowAnimation(window.winId())
    window.show()
    sys.exit(app.exec())