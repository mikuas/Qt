# coding:utf-8
import sys

from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit

from FluentWidgets import HBoxLayout
from qfluentwidgets import LineEdit
from qfluentwidgets.components.widgets.frameless_window import FramelessWindow

from qframelesswindow import TitleBarButton
from qframelesswindow.titlebar import MinimizeButton, CloseButton, MaximizeButton, StandardTitleBar
from qframelesswindow.utils import startSystemMove


class TitleBarBase(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.minBtn = None
        self.closeBtn = None
        self.maxBtn = None
        self._isDoubleClickEnabled = True
        self.setFixedHeight(32)
        self.hBoxLayout = HBoxLayout(self)

    def _connectSignalSlot(self):
        self.minBtn.clicked.connect(self.window().showMinimized)
        self.maxBtn.clicked.connect(self.__toggleMaxState)
        self.closeBtn.clicked.connect(self.window().close)

    def _initTitlebarButton(self, alignment=Qt.AlignRight):
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.addWidget(self.minBtn, 0, alignment)
        self.hBoxLayout.addWidget(self.maxBtn, 0, alignment)
        self.hBoxLayout.addWidget(self.closeBtn, 0, alignment)

    def _initTitleBar(self, alignment=Qt.AlignLeft):
        self.iconLabel = QLabel(self)
        self.iconLabel.setFixedSize(20, 20)
        self.hBoxLayout.insertSpacing(0, 10)
        self.hBoxLayout.insertWidget(1, self.iconLabel, 0, alignment)
        self.window().windowIconChanged.connect(self.setIcon)

        # add title label
        self.titleLabel = QLabel(self)
        self.hBoxLayout.insertWidget(2, self.titleLabel, 0, alignment)
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

    def mouseDoubleClickEvent(self, event):
        """ Toggles the maximization state of the window """
        if event.button() != Qt.LeftButton or not self._isDoubleClickEnabled:
            return

        self.__toggleMaxState()

    def mouseMoveEvent(self, e):
        if sys.platform != "win32" or not self.canDrag(e.position().toPoint()):
            return

        startSystemMove(self.window(), e.globalPosition().toPoint())

    def mousePressEvent(self, e):
        if sys.platform == "win32" or not self.canDrag(e.pos()):
            return

        startSystemMove(self.window(), e.globalPos())

    def __toggleMaxState(self):
        """ Toggles the maximization state of the window and change icon """
        if self.window().isMaximized():
            self.window().showNormal()
        else:
            self.window().showMaximized()

        if sys.platform == "win32":
            from qframelesswindow.utils.win32_utils import releaseMouseLeftButton
            releaseMouseLeftButton(self.window().winId())

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
        self.window().installEventFilter(self)
        self.minBtn = MinimizeButton(self)
        self.maxBtn = MaximizeButton(self)
        self.closeBtn = CloseButton(self)

        # connect signal slot
        self._connectSignalSlot()
        # add buttons to layout
        self._initTitlebarButton()

    def eventFilter(self, obj, event):
        if obj is self.window():
            if event.type() == QEvent.WindowStateChange:
                self.maxBtn.setMaxState(self.window().isMaximized())
                return False

        return super().eventFilter(obj, event)


class StandardTitleBar(TitleBar):
    """ Title bar with icon and title """

    def __init__(self, parent):
        super().__init__(parent)
        self._initTitleBar()
        self.hBoxLayout.insertStretch(3, 1)

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


class SearchTitleBar(TitleBarBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.window().installEventFilter(self)
        self.setFixedHeight(45)

        self.maxBtn = MaximizeButton(self)
        self.minBtn = MinimizeButton(self)
        self.closeBtn = CloseButton(self)

        self.searchBox = LineEdit(self)

        self._connectSignalSlot()
        self._initTitleBar(Qt.AlignLeft)
        self.hBoxLayout.insertWidget(3, self.searchBox, 1, Qt.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        self._initTitlebarButton(Qt.AlignTop | Qt.AlignRight)

    def __updateSearchBox(self):
        self.hBoxLayout.removeWidget(self.searchBox)
        self.hBoxLayout.insertWidget(3, self.searchBox, 1, Qt.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

    def setSearchBox(self, search: QLineEdit):
        self.searchBox.deleteLater()
        self.searchBox = search
        self.__updateSearchBox()
        return self

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.searchBox.setFixedWidth(self.width() / 3)

    def eventFilter(self, obj, e):
        if obj is self.window():
            if e.type() == QEvent.WindowStateChange:
                self.maxBtn.setMaxState(self.window().isMaximized())
                return False

        return super().eventFilter(obj, e)


class Window(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.setTitleBar(SearchTitleBar(self))


if __name__ == '__main__':

    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    window = Window()
    window.windowEffect.addWindowAnimation(window.winId())
    window.show()
    sys.exit(app.exec())