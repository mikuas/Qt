import sys
from typing import overload

from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLineEdit, QDialog, QLabel, QComboBox
from PySide6.QtCore import QPoint, QPointF, QPropertyAnimation, QUrl

# from Interface import WidgetInterface
from .Interface import WidgetInterface


class QUrlInterface(WidgetInterface):
    def __init__(self, parent=None):
        super().__init__(parent, True, setDialogBtn=True)
        self.button.setText("get url")
        self.edit.setPlaceholderText("输入URL")
        self.edit.textChanged.connect(lambda s: self.url.setUrl(s))
        
        self.url = QUrl('https://www.bilibili.com')
        
        self.button.clicked.connect(lambda: self.infos.append(self.url.url()))
        
        self.box.addWidget(self.edit)
        self.box.addWidget(self.button)
        self.box.addWidget(self.setDialogBtn)
        self.box.addWidget(self.infos)
        
        self.initSetDialog()
    
    def initSetDialog(self):
        texts = [
            "设置用户名",
            "设置密码",
            "设置主机名",
            "设置路径",
            "设置端口",
            "设置片段",
            "设置查询",
        ]
        schemes = [
            'http', 'file', 'https', 'mailto', 'MMS', 'ed2d', 'Flashget', 'thunder', 'gopher'
        ]
        functions = [
            lambda name: {
                self.url.setUserName(name),
                self.infos.append(f"已设置用户名: {name}")
            },
            lambda passwd: {
                self.url.setPassword(passwd),
                self.infos.append(f"已设置密码: {passwd}")
            },
            lambda host: {
                self.url.setHost(host),
                self.infos.append(f"已设置主机名: {host}")
            },
            lambda path: {
                self.url.setPath(path),
                self.infos.append(f"已设置路径: {path}")
            },
            lambda port: {
                self.url.setPort(int(port) if int(port) else 0),
                self.infos.append(f"已设置端口: {int(port) if int(port) else 0}")
            },
            lambda pd: {
                self.url.setFragment(pd),
                self.infos.append(f"已设置用片段: {pd}")
            },
            lambda search: {
                self.url.setQuery(search),
                self.infos.append(f"已设置用查询: {search}")
            },
        ]
        
        self.setDialog.box.addWidget(QLabel('设置传输协议'))
        cb = QComboBox(self)
        cb.setFixedHeight(35)
        cb.addItems(schemes)
        cb.currentTextChanged.connect(lambda s: {
            self.url.setScheme(s),
            self.infos.append(f"已设置传输协议为: {s}")
            })
        self.setDialog.box.addWidget(cb)
        for t, f in zip(texts, functions):
            self.setDialog.box.addWidget(QLabel(t))
            e = QLineEdit(self)
            e.setFixedHeight(35)
            e.textChanged.connect(f)
            e.textChanged.connect(self.button.click)
            self.setDialog.box.addWidget(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QUrlInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
    ...