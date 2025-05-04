import sys
from typing import overload

from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLineEdit, QDialog, QLabel, QComboBox, QCheckBox
from PySide6.QtCore import QPoint, QPointF, QPropertyAnimation, QUrl, Qt
from PySide6.QtGui import QPixmap, QDesktopServices

from Interface import WidgetInterface


class LinkLabel(WidgetInterface):
    def __init__(self, parent=None):
        super().__init__(parent, True, False)
        self.edit.setPlaceholderText("输入链接")
        self.edit.textChanged.connect(lambda t: {
            self.linkLabel.setText(f'<a href="{t}">点击打开链接</a>' if self.linkLabel.openExternalLinks() else t),
            self.infos.append("链接为: " + f'<a href="{t}">点击打开链接</a>' if self.linkLabel.openExternalLinks() else t)
        })
        
        self.linkLabel = QLabel(self)
        self.linkLabel.setText('<a href="https://www.bilibili.com">点击打开链接</a>')
        
        self.button.deleteLater()
        
        self.ol = QLabel("设置打开方式")
        self.c = QComboBox(self)
        self.c.setFixedHeight(35)
        self.c.addItems(['Auto', 'Activated', "Hovered"])
        self.c.currentTextChanged.connect(lambda t: self.infos.append(f"已设置打开方式为: {t}"))
        self.c.currentIndexChanged.connect(lambda index: self.linkLabel.setOpenExternalLinks(index == 0))
        
        # 设置打开超链接
        self.linkLabel.setOpenExternalLinks(True)
        
        self.box.addWidget(self.edit)
        self.box.addWidget(self.linkLabel, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.box.addWidget(self.ol, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.box.addWidget(self.c)
        self.box.addWidget(self.button)
        self.box.addWidget(self.infos)
        
        self.linkLabel.linkActivated.connect(lambda: 
            {QDesktopServices.openUrl(self.linkLabel.text()), print("Activated")} if self.c.currentText() == "Activated" else None
            )
        self.linkLabel.linkHovered.connect(lambda: 
            {QDesktopServices.openUrl(self.linkLabel.text()), print("Hovered")} if self.c.currentText() == "Hovered" else None
            )
    
        
class ImageLabel(WidgetInterface):
    def __init__(self, parent=None, enit=True):
        super().__init__(parent, enit, getDialogBtn=True)
        self.edit.setPlaceholderText("输入图片路径")
        
        self.imageLabel = QLabel(self)
        self.imageLabel.setMinimumSize(self.width(), 200)
        self.px = QPixmap()
        
        self.button.setText("Apply")
        self.button.clicked.connect(lambda: {
            self.infos.append(f"图片路径: {self.edit.text()}, 图片是否加载成功: {self.px.load(self.edit.text().replace('"', ''))}"),
            self.imageLabel.setPixmap(self.px)
        })
        
        self.box.addWidget(self.edit)
        self.box.addWidget(self.button)
        self.box.addWidget(self.getDialogBtn)
        self.box.addWidget(self.imageLabel)
        self.box.addWidget(self.infos)
        
        self.initGetDialog()
        
    def initGetDialog(self):
        l = QLabel("获取图像")
        b = QPushButton("Get")
        b.clicked.connect(lambda: {
            self.infos.append(f"图像: {self.imageLabel.pixmap()}")
        })
        
        self.getDialog.box.addWidget(l, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.getDialog.box.addWidget(b)
        
        
class QLabelInterface(WidgetInterface):
    def __init__(self, parent=None):
        super().__init__(parent, True, setDialogBtn=True)
        self.edit.setPlaceholderText("设置标签文字")
        
        self.button.setText("Apply")
        self.button.clicked.connect(lambda: {
            self.label.setText(self.edit.text()),
            self.infos.append(f"已设置标签文本为: {self.edit.text()}"),
            self.label.setToolTip(self.edit.text())
        })
        
        self.label = QLabel("Hello World!", self)
        self.label.setMinimumHeight(100)
        # 设置可选中
        self.label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse | Qt.TextInteractionFlag.TextSelectableByKeyboard)
        self.label.setSelection(10, 10)
        
        self.il = ImageLabel()
        self.ll = LinkLabel()
        
        self.imgBtn = QPushButton("Show ImageLabel Widget", self)
        self.imgBtn.clicked.connect(self.il.show)
        
        self.linkBtn = QPushButton("Show LinkLabel Widget")
        self.linkBtn.clicked.connect(self.ll.show)
        
        self.box.addWidget(self.edit)
        self.box.addWidget(self.button)
        self.box.addWidget(self.setDialogBtn)
        self.box.addWidget(self.imgBtn)
        self.box.addWidget(self.linkBtn)
        self.box.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.box.addWidget(self.infos)

        self.initSetDialog()

    def initSetDialog(self):
        texts = [
            "获取文本",
            "设置要显示的数值为10",
            "清空显示的内容",
            "获取选中的文字",
            "设置缩进量为10",
        ]
        functions = [
            lambda: {
                self.infos.append(f"标签的文本为: {self.label.text()}")
            },
            lambda: {
                self.label.setNum(10),
                self.infos.append("已设置要显示的数值为10")
            },
            lambda: {
                self.infos.append(f"已清空, 内容为: {self.label.text()}"),
                self.label.clear()
            },
            lambda: {
                self.infos.append(f"选中的文本为: {self.label.selectedText()}")
            },
            lambda: {
                self.infos.append("已设置缩进量为10")
            }
        ]
        
        for t, f in zip(texts, functions):
            self.setDialog.box.addWidget(QLabel(t))
            btn = QPushButton(t[:2])
            btn.clicked.connect(f)
            self.setDialog.box.addWidget(btn)
        
        align = [
            Qt.AlignmentFlag.AlignLeft,
            Qt.AlignmentFlag.AlignRight,
            Qt.AlignmentFlag.AlignBottom,
            Qt.AlignmentFlag.AlignTop,
            Qt.AlignmentFlag.AlignHCenter,
            Qt.AlignmentFlag.AlignVCenter
        ]
        ta = [
            'Qt.AlignmentFlag.AlignLeft',
            'Qt.AlignmentFlag.AlignRight',
            'Qt.AlignmentFlag.AlignBottom',
            'Qt.AlignmentFlag.AlignTop',
            'Qt.AlignmentFlag.AlignHCenter',
            'Qt.AlignmentFlag.AlignVCenter'
        ]
        
        l = QLabel("设置对齐方式")
        ac = QComboBox()
        ac.setFixedHeight(35)
        ac.addItems(ta)
        ac.currentIndexChanged.connect(lambda index: self.label.setAlignment(align[index]))
        self.setDialog.box.addWidget(l)
        self.setDialog.box.addWidget(ac)
        
        b = QHBoxLayout()
        l = QLabel("是否可以换行", self)
        c = QCheckBox()
        c.checkStateChanged.connect(lambda s: self.label.setWordWrap(s == Qt.CheckState.Checked)) # 设置是否可以换行
        b.addWidget(l)
        b.addWidget(c)
        self.setDialog.box.addLayout(b)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QLabelInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
    ...