from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QTextBrowser, QPushButton, QDialog


class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(600, 350)
        self.box = QVBoxLayout(self)
    
    def showEvent(self, arg__1):
        if self.isVisible():
            arg__1.ignore()
            return
        super().showEvent(arg__1)


class WidgetInterface(QWidget):
    def __init__(self, parent=None, enit=False, getDialogBtn=False, setDialogBtn=False):
        super().__init__(parent)
        self.setStyleSheet(
            """
            QPushButton, QLineEdit {
                height: 35px;
            }
            """
        )
        
        self.box = QVBoxLayout(self)
        self.infos = QTextBrowser(self)
        self.button = QPushButton(self)
        
        self.getDialog = Dialog(self)
        self.getDialog.setWindowTitle("获取属性对话框")
        self.setDialog = Dialog(self)
        self.setDialog.setWindowTitle("设置属性对话框")
        
        if enit:
            self.edit = QLineEdit(self)
            self.edit.setFixedHeight(35)

        if getDialogBtn:
            self.getDialogBtn = QPushButton("获取属性对话框", self)
            self.getDialogBtn.clicked.connect(self.getDialog.show)
        if setDialogBtn:
            self.setDialogBtn = QPushButton("设置属性对话框", self)
            self.setDialogBtn.clicked.connect(self.setDialog.show)
    
    def initLayout(self):
        self.box.addWidget(self.edit)
        self.box.addWidget(self.button)
        self.box.addWidget(self.infos)
    
    def verify(self): ...
    def initGetDialog(self): ...
    def initSetDialog(self): ...