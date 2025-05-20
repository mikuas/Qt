import sys
from typing import overload

from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLineEdit, QDialog, QLabel, QCheckBox
from PySide6.QtCore import QPoint, QPointF, QPropertyAnimation, QSize, QSizeF
from PySide6.QtGui import QFont, Qt

# from Interface import WidgetInterface
from .Interface import WidgetInterface


class Font(QFont):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, families: str, pointSize: int = -1, weight: int = -1, italic: bool = False):
        """_summary_

        Args:
            families (str): 字体名称
            pointSize (int, optional): 字体尺寸
            weight (int, optional): 粗细程度
            italic (bool, optional): 斜体
        """
        ...


class Funtion(QFont):
    # 设置粗体
    def setBold(self, arg__1: bool) -> None:
        return super().setBold(arg__1)
    
    # 设置斜体
    def setItalic(self, b: bool) -> None:
        return super().setItalic(b)
    
    # 设置字符间隙
    def setLetterSpacing(self, type: QFont.SpacingType, spacing: float) -> None:
        return super().setLetterSpacing(type, spacing)

    # 设置上划线
    def setOverline(self, arg__1: bool) -> None:
        return super().setOverline(arg__1)
    
    # 设置删除线
    def setStrikeOut(self, arg__1: bool) -> None:
        return super().setStrikeOut(arg__1)
    
    # 设置字体风格
    def setStyle(self, style: QFont.Style) -> None:
        return super().setStyle(style)
    
    # 设置下划线
    def setUnderline(self, arg__1: bool) -> None:
        return super().setUnderline(arg__1)
    
    # 设置字体粗细程度
    def setWeight(self, weight: QFont.Weight) -> None:
        return super().setWeight(weight)

    # 设置字间距
    def setWordSpacing(self, spacing: float) -> None:
        return super().setWordSpacing(spacing)
    ...


class QFontInterface(WidgetInterface):
    def __init__(self, parent=None):
        super().__init__(parent, setDialogBtn=True)
        self.button.deleteLater()
        self._font = QFont()
        self.infos.append("我是测试文字")
        
        self.edit1 = QLineEdit(self)
        self.edit1.setPlaceholderText("设置字符间隙")
        self.edit1.setFixedHeight(35)
        self.btn1 = QPushButton("apply", self)
        self.btn1.clicked.connect(lambda: {
            self._font.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, self.verify(self.edit1.text())),
            self.infos.setFont(self._font)
        })
        
        self.edit2 = QLineEdit(self)
        self.edit2.setPlaceholderText("设置字间距")
        self.edit2.setFixedHeight(35)
        self.btn2 = QPushButton("apply", self)
        self.btn2.clicked.connect(lambda: {
            self._font.setWordSpacing(self.verify(self.edit2.text())),
            self.infos.setFont(self._font)
            })
        
        self.box.addWidget(self.edit1)
        self.box.addWidget(self.btn1)
        self.box.addWidget(self.edit2)
        self.box.addWidget(self.btn2)
        self.box.addWidget(self.setDialogBtn)
        self.box.addWidget(self.infos)
        
        self.initSetDialog()
    
    def initSetDialog(self):
        texts = [
            "启用粗体",
            "启用斜体",
            "启用上划线",
            "启用删除线",
            "启用下划线"
        ]
        functions = [
            lambda state: {
                self._font.setBold(state is Qt.CheckState.Checked),
                self.infos.append("已启用粗体" if state is Qt.CheckState.Checked else "已取消启用粗体"),
                self.infos.setFont(self._font)
            },
            lambda state: {
                self._font.setItalic(state is Qt.CheckState.Checked),
                self.infos.append("已启用斜体" if state is Qt.CheckState.Checked else "已取消启用斜体"),
                self.infos.setFont(self._font)
            },
            lambda state: {
                self._font.setOverline(state is Qt.CheckState.Checked),
                self.infos.append("已启用上划线" if state is Qt.CheckState.Checked else "已取消启下划线"),
                self.infos.setFont(self._font)
            },
            lambda state: {
                self._font.setStrikeOut(state is Qt.CheckState.Checked),
                self.infos.append("已启用删除线" if state is Qt.CheckState.Checked else "已取消启删除线"),
                self.infos.setFont(self._font)
            },
            lambda state: {
                self._font.setUnderline(state is Qt.CheckState.Checked),
                self.infos.append("已启用下划线" if state is Qt.CheckState.Checked else "已取消启下划线"),
                self.infos.setFont(self._font)
            },
        ]
        
        for t, f, in zip(texts, functions):
            lable = QLabel(t, self)
            checkBox = QCheckBox(self)
            checkBox.setFixedSize(100, 100)
            checkBox.checkStateChanged.connect(f)
            
            hbox = QHBoxLayout()
            self.setDialog.box.addLayout(hbox)
            hbox.addWidget(lable, alignment=Qt.AlignmentFlag.AlignHCenter)
            hbox.addWidget(checkBox, alignment=Qt.AlignmentFlag.AlignHCenter)
    
    def verify(self, arg):
        try:
            spacing = float(arg)
            self.infos.append(f"已设置间距为 {spacing}")
            return spacing
        except ValueError:
            self.infos.append("已设置间距为 0")
            return 0
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QFontInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())