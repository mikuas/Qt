import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QAbstractItemModel, Qt



class Window(QWidget):
    def __init__(self):
        super().__init__()
        """
        Roles
        
        Qt.DisplayRole          文本
        Qt.DecorationRole       图标
        Qt.EditRole             编辑显示文本
        Qt.ToolTipRole          提示文本
        Qt.StatusTipRole        状态提示文本
        Qt.FontRole             字体
        Qt.TextAlignmentRole    文本对齐方式
        Qt.BackgroundColorRole  背景颜色
        Qt.ForegroundColorRole  前景颜色
        Qt.CheckStateRole       复选框状态
        
        """
        
        self.model = QAbstractItemModel(self)
        self.model.setData(self.model.index(0, 0), "Hello World", Qt.ItemDataRole.TextAlignmentRole)
        
        self.model.data(self.model.index(0, 0), Qt.ItemDataRole.TextAlignmentRole)
        ...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())