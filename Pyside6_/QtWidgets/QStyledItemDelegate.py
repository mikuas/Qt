# coding:utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QStyledItemDelegate, \
    QListView, QListWidget, QHBoxLayout


class StyleItemDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        return super().createEditor(parent, option, index)
    
    def setEditorData(self, editor, index):
        return super().setEditorData(editor, index)
    
    def updateEditorGeometry(self, editor, option, index):
        return super().updateEditorGeometry(editor, option, index)
    
    def paint(self, painter, option, index):
        # 这里的 option 就是 QStyleOptionViewItem
        # QStyleOptionViewItem 属性
        
        print(f"项的背景画刷[backgroundBrush]: {option.backgroundBrush}", '\n', 
              f"项的勾选状态[checkState]: {option.checkState}", '\n',
              f"项的图标对齐方式[decorationAlignment]: {option.decorationAlignment}", '\n',
              f"项的图标位置[decorationPosition]: {option.decorationPosition}", '\n',
              f"项的图标尺寸[decorationSize]: {option.decorationSize}", '\n',
              f"项的文字对其方式[displayAlignment]: {option.displayAlignment}", '\n',
              f"项所具有的特征[features]: {option.features}", '\n',
              f"项的字体[font]: {option.font}", '\n',
              f"项图标[icon]: {option.icon}", '\n',
              f"项的模型索引[index]: {option.index}", '\n',
              f"项是否显示图标[showDecorationSelected]: {option.showDecorationSelected}", '\n',
              f"项显示的文本[text]: {option.text}", '\n',
              f"省略号的模式[textElideMode]: {option.textElideMode}", '\n',
              f"项在行中的位置[viewItemPosition]: {option.viewItemPosition}", '\n',
              f"布局方向[direction]: {option.direction}", '\n',
              f"调色板[palette]: {option.palette}", '\n',
              f"项的矩形区域[rect]: {option.rect}", '\n',
              f"项的窗口类型[styleObject]: {option.styleObject}", '\n',
              f"版本[version]: {option.version}",
              end="\n\n\n\n\n"
              )
        
        painter.save()
        painter.restore()
        
        return super().paint(painter, option, index)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.box = QHBoxLayout(self)
        
        self.listView = QListView(self)
        self.listWidget = QListWidget(self)
        
        self.box.addWidget(self.listView)
        self.box.addWidget(self.listWidget)

        self.initListView()
        self.initListWidget()
    
    def initListView(self): ...
    
    def initListWidget(self):
        self.listWidget.setItemDelegate(StyleItemDelegate(self))
        self.listWidget.addItems([
            f"Item {_}" for _ in range(1, 1001)
        ])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())