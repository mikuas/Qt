import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QObject, Signal


class SignalWidget(QWidget): # QObject
    noArgSignal = Signal()
    intArgSignal = Signal(int)
    floatArgSignal = Signal(float)
    stringArgSignal = Signal(str)
    int_float_string_ArgsSignal = Signal(int, float, str)
    listArgSignal = Signal(list)
    dictArgSignal = Signal(dict)
    # 重载信号
    int_or_string_ArgsSignal = Signal([int], [str]) # 两个信号
    int_and_string_or_str_or_list_ArgSignal = Signal([int, str], [str], [list])
    no_arg_or_bool_ArgSignal = Signal([], [bool])
    
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.noArgSignal.connect(lambda: print("No Args Signal"))
        self.intArgSignal.connect(lambda arg: print(f"arg: {arg}, type: {type(arg)}"))
        self.floatArgSignal.connect(lambda arg: print(f"arg: {arg}, type: {type(arg)}"))
        self.stringArgSignal.connect(lambda arg: print(f"arg: {arg}, type: {type(arg)}"))
        self.int_float_string_ArgsSignal.connect(
            lambda arg__1, arg__2, arg__3:
                print(f"arg: {arg__1, arg__2, arg__3}, type: {[type(arg) for arg in [arg__1, arg__2, arg__3]]}")
                )
        self.listArgSignal.connect(lambda arg: print(f"arg: {arg}, type: {type(arg)}"))
        self.dictArgSignal.connect(lambda arg: print(f"arg: {arg}, type: {type(arg)}"))
        self.int_or_string_ArgsSignal.connect(lambda arg: print(f"arg: {arg}, type: {type(arg)}"))
        # self.int_and_string_or_str_or_list_ArgSignal.connect(lambda arg: print(f"arg: {arg}, type: {type(arg)}"))
        
        self.noArgSignal.emit()
        self.intArgSignal.emit(1145)
        self.floatArgSignal.emit(19.19)
        self.stringArgSignal.emit('Hello World!')
        self.int_float_string_ArgsSignal.emit(1, 1, '45')
        self.listArgSignal.emit([n for n in range(10)])
        self.dictArgSignal.emit({n: n ** 2 for n in range(10)})
        self.int_or_string_ArgsSignal.emit(1145) # int


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = SignalWidget()
    window.show()
    sys.exit(app.exec())
    pass