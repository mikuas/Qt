# coding:utf-8
import sys
from ctypes import cast
from ctypes.wintypes import MSG, LPRECT
from typing import Union

import win32con
import win32gui

from PySide6.QtCore import Qt, QSize, QRect, QEvent, QPropertyAnimation, QEasingCurve, QTimer, Signal
from PySide6.QtGui import QIcon, QCursor, QPainter, QColor, QPainterPath
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit

from FluentWidgets import HBoxLayout, SideNavWidget, TitleLabel, FluentIcon, NavigationItemPosition, Icon, PushButton, \
    TransparentToolButton, SearchLineEdit, PasswordLineEdit, TextEdit, isDarkTheme, SplitFluentWindow
from qfluentwidgets import LineEdit

from qframelesswindow import TitleBar, AcrylicWindow, TitleBarButton
from qframelesswindow.titlebar import MinimizeButton, CloseButton, MaximizeButton
from qframelesswindow.utils.win32_utils import Taskbar
from qframelesswindow.utils import win32_utils as win_utils, startSystemMove
from qframelesswindow.windows import WindowsWindowEffect, LPNCCALCSIZE_PARAMS


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


class WindowsFramelessWindowBase:
    """ Frameless window base class for Windows system """

    BORDER_WIDTH = 5

    def __init__(self, parent=None):
        super().__init__(parent)
        self._isSystemButtonVisible = False

    def _initFrameless(self):
        self.windowEffect = WindowsWindowEffect(self)
        self._isResizeEnabled = True
        self.titleBar = StandardTitleBar(self)

        self.updateFrameless()
        self.titleBar.raise_()

        # solve issue #5
        self.windowHandle().screenChanged.connect(self.__onScreenChanged)

    def updateFrameless(self):
        """ update frameless window """
        # self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        # add DWM shadow and window animation
        self.windowEffect.addWindowAnimation(self.winId())
        if not isinstance(self, AcrylicWindow):
            self.windowEffect.addShadowEffect(self.winId())

    def setTitleBar(self, titleBar):
        """ set custom title bar

        Parameters
        ----------
        titleBar: TitleBar
            title bar
        """
        self.titleBar.deleteLater()
        self.titleBar.hide()
        self.titleBar = titleBar
        self.titleBar.setParent(self)
        self.titleBar.raise_()

    def setResizeEnabled(self, isEnabled: bool):
        """ set whether resizing is enabled """
        self._isResizeEnabled = isEnabled

    def isSystemButtonVisible(self):
        """ Returns whether the system title bar button is visible """
        return self._isSystemButtonVisible

    def setSystemTitleBarButtonVisible(self, isVisible):
        """ set the visibility of system title bar button, only works for macOS """
        pass

    def systemTitleBarRect(self, size: QSize) -> QRect:
        """ Returns the system title bar rect, only works for macOS

        Parameters
        ----------
        size: QSize
            original system title bar rect
        """
        return QRect(0, 0, size.width(), size.height())

    def nativeEvent(self, eventType, message):
        """ Handle the Windows message """
        msg = MSG.from_address(message.__int__())
        if not msg.hWnd:
            return False, 0

        if msg.message == win32con.WM_NCHITTEST and self._isResizeEnabled:
            pos = QCursor.pos()
            xPos = pos.x() - self.x()
            yPos = pos.y() - self.y()
            w = self.frameGeometry().width()
            h = self.frameGeometry().height()

            # fixes https://github.com/zhiyiYo/PyQt-Frameless-Window/issues/98
            bw = 0 if win_utils.isMaximized(msg.hWnd) or win_utils.isFullScreen(msg.hWnd) else self.BORDER_WIDTH
            lx = xPos < bw
            rx = xPos > w - bw
            ty = yPos < bw
            by = yPos > h - bw
            if lx and ty:
                return True, win32con.HTTOPLEFT
            elif rx and by:
                return True, win32con.HTBOTTOMRIGHT
            elif rx and ty:
                return True, win32con.HTTOPRIGHT
            elif lx and by:
                return True, win32con.HTBOTTOMLEFT
            elif ty:
                return True, win32con.HTTOP
            elif by:
                return True, win32con.HTBOTTOM
            elif lx:
                return True, win32con.HTLEFT
            elif rx:
                return True, win32con.HTRIGHT
        elif msg.message == win32con.WM_NCCALCSIZE:
            if msg.wParam:
                rect = cast(msg.lParam, LPNCCALCSIZE_PARAMS).contents.rgrc[0]
            else:
                rect = cast(msg.lParam, LPRECT).contents

            isMax = win_utils.isMaximized(msg.hWnd)
            isFull = win_utils.isFullScreen(msg.hWnd)

            # adjust the size of client rect
            if isMax and not isFull:
                ty = win_utils.getResizeBorderThickness(msg.hWnd, False)
                rect.top += ty
                rect.bottom -= ty

                tx = win_utils.getResizeBorderThickness(msg.hWnd, True)
                rect.left += tx
                rect.right -= tx

            # handle the situation that an auto-hide taskbar is enabled
            if (isMax or isFull) and Taskbar.isAutoHide():
                position = Taskbar.getPosition(msg.hWnd)
                if position == Taskbar.LEFT:
                    rect.top += Taskbar.AUTO_HIDE_THICKNESS
                elif position == Taskbar.BOTTOM:
                    rect.bottom -= Taskbar.AUTO_HIDE_THICKNESS
                elif position == Taskbar.LEFT:
                    rect.left += Taskbar.AUTO_HIDE_THICKNESS
                elif position == Taskbar.RIGHT:
                    rect.right -= Taskbar.AUTO_HIDE_THICKNESS

            result = 0 if not msg.wParam else win32con.WVR_REDRAW
            return True, result

        return False, 0

    def __onScreenChanged(self):
        hWnd = int(self.windowHandle().winId())
        win32gui.SetWindowPos(hWnd, None, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_FRAMECHANGED)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.titleBar.resize(self.width(), self.titleBar.height())


class SearchTitleBar(TitleBarBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.window().installEventFilter(self)
        self.setFixedHeight(45)
        self.window().installEventFilter(self)

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


class FramelessWindow(WindowsFramelessWindowBase, QWidget):
    def __init__(self):
        super().__init__()
        self._initFrameless()

''
class ExpandNav(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        from FluentWidgets import NavigationInterface, PopUpStackedWidget
        from qfluentwidgets import PopUpAniStackedWidget

        class SW(PopUpAniStackedWidget):
            def __init__(self, parent):
                super().__init__(parent)

            def paintEvent(self, e):
                super().paintEvent(e)
                painter = QPainter(self)
                painter.setPen(Qt.PenStyle.NoPen)
                painter.setBrush(QColor(255, 255, 255))
                painter.drawRoundedRect(self.rect(), 12, 12)

        self.navigationInterface = NavigationInterface(self, showReturnButton=True)
        self.stackedWidget = SW(parent=self)

        self.box = HBoxLayout(self)

        self.box.addWidget(self.navigationInterface)
        self.box.addWidget(self.stackedWidget)

        self.navigationInterface.setMinimumExpandWidth(200)
        self.navigationInterface.setExpandWidth(256)

        self.setContentsMargins(0, 0, 0, 0)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.setContentsMargins(0, 0, 0, 0)
        self.navigationInterface.setContentsMargins(0, 0, 0, 0)

    def addSubInterface(self, routeKey: str, title: str,  widget: QWidget, icon: Union[str, QIcon, FluentIcon] = None):
        self.navigationInterface.addItem(routeKey, icon, title, lambda: self._onClick(widget),
                                         tooltip=title)
        self.stackedWidget.addWidget(widget)

    def _onClick(self, w: QWidget):
        self.stackedWidget.setCurrentWidget(w)


class Window(FramelessWindow):
    def __init__(self):
        super().__init__()
        from FluentWidgets import FluentWindow
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.windowEffect.addWindowAnimation(self.winId())
        self.windowEffect.setMicaEffect(self.winId(), isAlt=True)

        self.setMinimumSize(800, 520)

        self.box = HBoxLayout(self)
        self.setTitleBar(SearchTitleBar(self).setSearchBox(SearchLineEdit(self)))

        self.setWindowIcon(Icon(FluentIcon.GITHUB))
        self.setWindowTitle("HELLO")

        self.setContentsMargins(0, 48, 0, 0)
        self.nav = ExpandNav(self)
        self.box.addWidget(self.nav)

        self.nav.setMinimumWidth(400)

        class cw(QWidget):
            def __init__(self):
                super().__init__()
                l = HBoxLayout(self)
                l.addWidget(TitleLabel("INTERFACE"), alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

            def _updateAcrylicColor(self):
                if isDarkTheme():
                    tintColor = QColor(32, 32, 32, 200)
                    luminosityColor = QColor(0, 0, 0, 0)
                else:
                    tintColor = QColor(255, 255, 255, 180)
                    luminosityColor = QColor(255, 255, 255, 0)

                self.acrylicBrush.tintColor = tintColor
                self.acrylicBrush.luminosityColor = luminosityColor

        self.nav.addSubInterface("INTERFACE1", "INTERFACE", cw(), FluentIcon.HOME)
        self.nav.addSubInterface("INTERFACE2", "INTERFACE", TitleLabel("INTERFACE"), FluentIcon.HOME)
        self.nav.addSubInterface("INTERFACE3", "INTERFACE", TitleLabel("CIALLOWORLD"), FluentIcon.HOME)


if __name__ == '__main__':

    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    window = Window()
    # window = SplitFluentWindow()
    window.windowEffect.addWindowAnimation(window.winId())
    window.show()
    sys.exit(app.exec())