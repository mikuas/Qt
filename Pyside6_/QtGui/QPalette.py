import sys

from typing import overload


from PySide6.QtWidgets import QApplication, QWidget, QTextBrowser, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QComboBox
from PySide6.QtGui import QPalette, QColor, QCursor

# from Interface import WidgetInterface
from .Interface import WidgetInterface



class QPaletteInterface(WidgetInterface):
    def __init__(self, parent=None):
        super().__init__(parent, True, setDialogBtn=True)
        self._role = QPalette.ColorRole.Text
        
        self.edit.setPlaceholderText("设置文字调色板颜色")
        
        self.sbtn = QPushButton('set palette', self)
        self.sbtn.clicked.connect(lambda: {
            self._palette.setColor(self._role, QColor(self.edit.text())),
            self.updatePalette(f"已设置调色板为: {self.edit.text()}色")
            
        })
        
        self.button.setText("get palette")
        self.button.clicked.connect(
            lambda: self.updatePalette(str(self._palette.color(QPalette.ColorGroup.Active, self._role)))
            )
        
        self.box.addWidget(self.edit)
        self.box.addWidget(self.sbtn)
        self.box.addWidget(self.button)
        self.box.addWidget(self.setDialogBtn)
        self.box.addWidget(self.infos)
        
        self._palette = QPalette()
        self.initSetDialog()
    
    def initSetDialog(self):
        items = [
            QPalette.ColorRole.WindowText,
            QPalette.ColorRole.Button,    
            QPalette.ColorRole.Light,          
            QPalette.ColorRole.Midlight,       
            QPalette.ColorRole.Dark,
            QPalette.ColorRole.Mid,          
            QPalette.ColorRole.Text,           
            QPalette.ColorRole.BrightText,     
            QPalette.ColorRole.ButtonText,     
            QPalette.ColorRole.Base,           
            QPalette.ColorRole.Window,         
            QPalette.ColorRole.Shadow,         
            QPalette.ColorRole.Highlight,      
            QPalette.ColorRole.HighlightedText,
            QPalette.ColorRole.Link,           
            QPalette.ColorRole.LinkVisited,    
            QPalette.ColorRole.AlternateBase,  
            QPalette.ColorRole.NoRole,         
            QPalette.ColorRole.ToolTipBase,    
            QPalette.ColorRole.ToolTipText,    
            QPalette.ColorRole.PlaceholderText,
            QPalette.ColorRole.Accent,              
            QPalette.ColorRole.NColorRoles    
        ]
        texts =[
            "窗口前景色",
            "按钮的背景色",
            "与控件的3D效果和阴影效果相关的颜色",
            "与控件的3D效果和阴影效果相关的颜色",
            "与控件的3D效果和阴影效果相关的颜色",
            "与控件的3D效果和阴影效果相关的颜色",
            "文本输入控件的前景色",
            "文本的对比色",
            "按钮的前景色",
            "文本输入控件背景色(如QTextEdit)",
            "窗口控件的背景色",
            "与控件的3D效果和阴影效果相关的颜色",
            "所选物体的背景色",
            "所选物体的前景色",
            "超链接的颜色",
            "超链接访问后的颜色",
            "多行输入输出控件行交替背景色(如QListWidget)",
            "NONE",
            "提示信息的背景色",
            "提示信息的前景色",
            "输入框中占位文本的颜色",
            "NONE",
            "NONE"
        ]
        
        c = QComboBox(self)
        c.addItems([str(item) for item in items])
        c.setCurrentText(str(QPalette.ColorRole.Text))
        c.currentIndexChanged.connect(lambda index: {
            self.updateRole(items[index]),
            l.setText(texts[index])
            })
        self.setDialog.box.addWidget(c)
        l = QLabel(self)
        self.setDialog.box.addWidget(l)
        
    def updateRole(self, role):
        self._role = role
    
    def updatePalette(self, text):
        self.infos.setPalette(self._palette)
        self.infos.append(text)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QPaletteInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())