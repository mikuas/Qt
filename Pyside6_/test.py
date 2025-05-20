import sys

from PySide6.QtGui import QColor, Qt
from PySide6.QtWidgets import QApplication
from FluentWidgets import SideNavWidget, TitleLabel, FluentIcon, SmoothSwitchNavWidget
from enum import Enum
from typing import overload, Dict, List, Tuple, Set, Literal, Any, AnyStr, DefaultDict, final, \
    LiteralString, ByteString, Union


class Demo(Enum):

    AnyByteString = ByteString
    AnyDict = Dict
    AnyList = List
    AnyTuple = Tuple
    AnySet = Set
    AnyLiteral = Literal
    AnyString = AnyStr
    AnyDefaultDict = DefaultDict
    Final = final
    OverLoad = overload

    @overload
    def value(self):
        return "Hello World"

    @overload
    def value(self):
        return b"Hello World"

    def value(self):
        return None

class Test:

    ARGS = []

    def __init__(self):
        super().__init__()
        value = None
        inter = None
        ver = Enum

        inter.split(ver)

        print(value)

    def setValue(self, value: Any): self.value = value

    def AnyValue(self, value):
        value = value
        inter = value
        print(inter)

        result = []
        for e in result:
            print(e)


    def test(self, arg: int | float | str | dict | list |
             set | tuple | Any | None): ...

    @overload
    def value(self):
        return fr"{self.value()}"

    @overload
    def value(self, args: Union[int, float, str, dict, list, set, tuple, Any, None]): ...

    @overload
    def value(self, args: List): ...

    @overload
    def value(self, args: Any): ...

    def value(self, args: Any): ...

    def get(self):
        return {
            {
                {
                    {
                        {
                            [
                                [
                                    [
                                        [
                                            []
                                        ]
                                    ]
                                ]
                            ]
                        }
                    }
                }
            }
        }


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SmoothSwitchNavWidget()
    window.resize(800, 520)
    window.show()

    items = {
        "HOME INTERFACE": FluentIcon.HOME,
        "MUSIC INTERFACE": FluentIcon.MUSIC,
        "GITHUB INTERFACE": FluentIcon.GITHUB,
        "SETTING INTERFACE": FluentIcon.SETTING
    }

    for k, v in items.items():
        if k == 'SETTING INTERFACE':
            window.addSubInterface(k, '', TitleLabel(k), v)
            continue
        window.addSubInterface(k, k, TitleLabel(k), v)

    window.setNavigationAlignment(Qt.AlignmentFlag.AlignLeft)

    setting = list(window.navigationBar.getAllWidget().values())[-1]
    window.navigationBar._widgetLayout.addWidget(setting, 1, Qt.AlignmentFlag.AlignRight)
    # window.navigationBar._widgetLayout.removeWidget(setting)
    # window.navigationBar._widgetLayout.addWidget(setting, alignment=Qt.AlignmentFlag.AlignRight)

    window.setCurrentWidget('HOME INTERFACE')
    sys.exit(app.exec())
    ...
