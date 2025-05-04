# coding:utf-8

import sys

from PySide6.QtGui import QFont, Qt, QTextCharFormat, QTextDocument, QColor, QTextImageFormat
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QScrollArea, QVBoxLayout, QLabel, QLineEdit, QPushButton

from Interface import WidgetInterface


class QTextEditInterface(WidgetInterface):
    def __init__(self):
        super().__init__(setDialogBtn=True, getDialogBtn=True)
        self.button.deleteLater()

        self.textEdit = QTextEdit(self)
        self.textEdit.createStandardContextMenu()

        charFormat = QTextCharFormat()

        imageFormat = QTextImageFormat()
        imageFormat.setName(r"C:\Users\Administrator\OneDrive\Pictures\1.jpg")
        imageFormat.setWidth(1000)
        imageFormat.setHeight(600)

        self.textEdit.textCursor().insertImage(imageFormat)

        # self.textEdit.setCurrentCharFormat(charFormat)
        #
        # document = QTextDocument("DOCUMENT")
        # self.textEdit.setDocument(document)


        # 设置只读
        # self.textEdit.setReadOnly(True)

        #
        # font = QFont()
        # font.setPointSize(24)
        # self.textEdit.setFont(font)
        #
        # self.textEdit.setTextColor('pink')
        self.zone = QWidget()
        self.scrollLayout = QVBoxLayout(self.zone)
        self.scroll = QScrollArea(self)
        self.scroll.setWidget(self.zone)
        self.scroll.setWidgetResizable(True)

        self.box.addWidget(self.textEdit)
        self.box.addWidget(self.setDialogBtn)
        self.box.addWidget(self.getDialogBtn)
        self.box.addWidget(self.infos)

        self.initSetDialog()
        self.initGetDialog()

    def initSetDialog(self):
        self.setDialog.box.addWidget(self.scroll)

        self.edits = []

        texts = [
            "设置显示的文字",
            "添加文本",
            "设置纯文本文字",
            "插入文本",
            "设置HTML格式文字",
            "插入HTML格式文字",
            "查找",
            "设置光标宽度",
            "设置table后退距离",
            "设置背景色",
            "设置文字颜色",
            "放大",
            "缩小"
        ]
        functions = [
            lambda: {
                self.textEdit.setText(self.edits[0].text()),
                self.infos.append(f"已设置显示的文字为: {self.edits[0].text()}")
            },
            lambda: {
                self.textEdit.append(self.edits[1].text()),
                self.infos.append(f"已添加文本: {self.edits[1].text()}")
            },
            lambda: {
                self.textEdit.setPlainText(self.edits[2].text()),
                self.infos.append(f"已设置纯文本文字为: {self.edits[2].text()}")
            },
            lambda: {
                self.textEdit.insertPlainText(self.edits[3].text()),
                self.infos.append(f"已插入纯文本文字为: {self.edits[3].text()}")
            },
            lambda: {
                self.textEdit.setHtml(self.edits[4].text()),
                self.infos.append(f"已设置HTML格式文字为: {self.edits[4].text()}")
            },
            lambda: {
                self.textEdit.insertHtml(self.edits[5].text()),
                self.infos.append(f"已插入HTML格式文字为: {self.edits[5].text()}")
            },
            lambda: {
                self.infos.append("存在" if self.textEdit.find(self.edits[6].text()) else "不存在")
            },
            lambda: {
                self.textEdit.setCursorWidth(self.verify(self.edits[7].text())),
                self.infos.append(f"已设置光标宽度为: {self.verify(self.edits[7].text())}")
            },
            lambda: {
                self.textEdit.setTabStopDistance(self.verify(self.edits[8].text())),
                self.infos.append(f"已设置table后退距离为: {self.verify(self.edits[8].text())}")
            },
            lambda: {
                self.textEdit.setTextBackgroundColor(QColor(self.edits[9].text())),
                self.infos.append(f"已设置背景色为: {self.edits[9].text()}")
            },
            lambda: {
                self.textEdit.setTextColor(QColor(self.edits[10].text())),
                self.infos.append(f"已设置文字颜色为: {self.edits[10].text()}")
            },
            lambda: {
                self.textEdit.zoomIn(self.verify(self.edits[11].text())),
                self.infos.append(f"已放大: {self.verify(self.edits[11].text())} 倍")
            },
            lambda: {
                self.textEdit.zoomOut(self.verify(self.edits[12].text())),
                self.infos.append(f"已缩小: {self.verify(self.edits[12].text())} 倍")
            }
        ]
        for t, f in zip(texts, functions):
            label = QLabel(t)
            edit = QLineEdit()
            self.edits.append(edit)
            button = QPushButton("确定")
            button.clicked.connect(f)

            self.scrollLayout.addWidget(label, alignment=Qt.AlignmentFlag.AlignHCenter)
            self.scrollLayout.addWidget(edit)
            self.scrollLayout.addWidget(button)
            self.scrollLayout.addWidget(QLabel("----------------------------------------------------------------------------------------------------"), alignment=Qt.AlignmentFlag.AlignHCenter)


        texts = [
            ""
        ]
        ...

    def initGetDialog(self):
        # self.setDialog.box
        texts = [
            "获取纯文本文字",
            "获取HTML格式文本",
            "获取文字颜色",
        ]
        functions = [
            lambda: {
                self.infos.append(f"已获取纯文本文字为: {self.textEdit.toPlainText()}")
            },
            lambda: {
                self.infos.append(f"已获取HTML格式文本为: {self.textEdit.toHtml()}")
            },
            lambda: {
                self.infos.append(f"已获取文字颜色为: {self.textEdit.textColor()}")
            }
        ]
        for t, f in zip(texts, functions):
            label = QLabel(t)
            button = QPushButton("确定")
            button.clicked.connect(f)
            self.getDialog.box.addWidget(label, alignment=Qt.AlignmentFlag.AlignHCenter)
            self.getDialog.box.addWidget(button)
        ...

    def verify(self, text):
        try:
            return int(text)
        except ValueError:
            return 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QTextEditInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
    ...