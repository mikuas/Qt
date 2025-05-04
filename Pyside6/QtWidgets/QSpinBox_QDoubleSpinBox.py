# coding:utf-8

import sys
from PySide6.QtCore import QPoint
from PySide6.QtGui import QFont, Qt, QTextCharFormat, QTextDocument, QColor, QTextImageFormat, QAction
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QScrollArea, QVBoxLayout, QLabel, QLineEdit, QPushButton, QPlainTextEdit, QSpinBox, QDoubleSpinBox

from Interface import WidgetInterface


class QSpinBox_QDoubleSpinBox_Interface(WidgetInterface):
    def __init__(self):
        super().__init__(setDialogBtn=True)
        self.button.deleteLater()
        self.setStyleSheet(self.styleSheet() +
                           """
                           QSpinBox, QDoubleSpinBox {
                                height: 35px;
                                border-radius: 8px;
                           }
                          QSpinBox::up-button, QDoubleSpinBox::up-button {
                                width: 25px;
                                height: 16px;
                                /* image: url("C:/Users/Administrator/Downloads/_rc/images/spin_box/Up_black.svg"); */
                            }
                            QSpinBox::down-button, QDoubleSpinBox::down-button {
                                width: 25px;
                                height: 16px;
                            }
                           """)

        self.zone = QWidget()
        self.scrollLayout = QVBoxLayout(self.zone)
        self.scroll = QScrollArea(self)
        self.scroll.setWidget(self.zone)
        self.scroll.setWidgetResizable(True)

        self.spinBox = QSpinBox(self)
        # self.spinBox.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)

        # 设置加速
        self.spinBox.setAccelerated(True)

        self.doubleSpinBox = QDoubleSpinBox(self)

        self.spinBox.setRange(0, 999999)
        self.spinBox.setSuffix('kg')
        self.spinBox.setPrefix('￥')

        self.box.addWidget(self.spinBox)
        self.box.addWidget(self.doubleSpinBox)
        self.box.addWidget(self.setDialogBtn)
        self.box.addWidget(self.infos)

        self.initSetDialog()

    def initSetDialog(self):
        self.setDialog.box.addWidget(self.scroll)
        self.edits = []
        texts = [
            "设置当前的值",
            "设置整数进制位如 2, 8, 16 默认为10",
            "设置小数位数",
            "最大值",
            "最小值",
            "设置步长",
            "设置前缀",
            "设置后缀",
        ]
        functions = [
            lambda: {
                self.spinBox.setValue(self.verify(self.edits[0].text())),
                self.doubleSpinBox.setValue(self.verify(self.edits[0].text())),
                self.infos.append(f"已设置当前值为: {self.verify(self.edits[0].text())}")
            },
            lambda: {
                self.spinBox.setDisplayIntegerBase(10 if self.verify(self.edits[1].text()) == 0 else self.verify(self.edits[1].text())),
                self.infos.append(f"已设置进制为: {10 if self.verify(self.edits[1].text()) == 0 else self.verify(self.edits[1].text())}")
            },
            lambda: {
                self.doubleSpinBox.setDecimals(self.verify(self.edits[2].text())),
                self.infos.append(f"已设置小数位数为: {self.verify(self.edits[2].text())}")
            },
            lambda: {
                self.spinBox.setMaximum(self.verify(self.edits[3].text())),
                self.doubleSpinBox.setMaximum(self.verify(self.edits[3].text())),
                self.infos.append(f"已设置最大值为: {self.verify(self.edits[3].text())}")
            },
            lambda: {
                self.spinBox.setMinimum(self.verify(self.edits[4].text())),
                self.doubleSpinBox.setMinimum(self.verify(self.edits[4].text())),
                self.infos.append(f"已设置最小值为: {self.verify(self.edits[4].text())}")
            },
            lambda: {
                self.spinBox.setSingleStep(self.verify(self.edits[5].text())),
                self.doubleSpinBox.setSingleStep(self.verify(self.edits[5].text())),
                self.infos.append(f"已设置步长为: {self.verify(self.edits[5].text())}")
            },
            lambda: {
                self.spinBox.setPrefix(self.edits[6].text()),
                self.doubleSpinBox.setPrefix(self.edits[6].text()),
                self.infos.append(f"已设置前缀为: {self.edits[6].text()}")
            },
            lambda: {
                self.spinBox.setSuffix(self.edits[7].text()),
                self.doubleSpinBox.setSuffix(self.edits[7].text()),
                self.infos.append(f"已设置后缀为: {self.edits[7].text()}")
            }
        ]
        for t, f in zip(texts, functions):
            edit = QLineEdit(self)
            self.edits.append(edit)

            self.scrollLayout.addWidget(QLabel(t, self), alignment=Qt.AlignmentFlag.AlignHCenter)
            self.scrollLayout.addWidget(edit)
            self.scrollLayout.addWidget(QPushButton("确定", self, clicked=f))

    def verify(self, text):
        try:
            return int(text)
        except ValueError:
            return 0

        ...

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QSpinBox_QDoubleSpinBox_Interface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
    ...