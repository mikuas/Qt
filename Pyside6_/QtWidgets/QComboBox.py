# coding:utf-8

import sys

from PySide6.QtGui import QFont, Qt, QTextCharFormat, QTextDocument, QColor, QTextImageFormat, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QScrollArea, QVBoxLayout, QLabel, QLineEdit, \
    QPushButton, QComboBox

from Interface import WidgetInterface


class QComboBoxInterface(WidgetInterface):
    def __init__(self):
        super().__init__(setDialogBtn=True, getDialogBtn=True)
        self.button.deleteLater()

        self.comboBox = QComboBox(self)
        self.comboBox.addItems(['item1', 'item2', 'item3', 'item4', 'item5'])

        # 设置是否可编辑
        self.comboBox.setEditable(True)

        # 设置项最大数量, 超过显示滚动条
        self.comboBox.setMaxVisibleItems(3)

        self.comboBox.setMinimumContentsLength(50)
        self.comboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        # 插入策略
        # self.comboBox.setInsertPolicy(QComboBox.InsertPolicy.InsertAtBottom)

        # 设置项最大数量, 超过不显示
        # self.comboBox.setMaxCount(3)

        # 输入内容合法性验证
        # self.comboBox.setValidator()

        # user data
        self.comboBox.addItem(QIcon(r"C:\Users\Administrator\OneDrive\Pictures\1735135361456.jpg"), 'icon',
                              userData='im is user data')

        self.comboBox.setStyleSheet(
            """
            QComboBox {
                height: 35px;
                border-radius: 8px;
            }
            """
        )

        self.comboBox.currentIndexChanged.connect(lambda index:
                                                  self.infos.append(
                                                      # get user data
                                                      f"current item userData: {self.comboBox.itemData(index)}"
                                                  ))
        self.comboBox.currentTextChanged.connect(lambda item:
                                                 self.infos.append(
                                                     f"current item text: {item}"
                                                 ))

        self.box.addWidget(self.comboBox)
        self.box.addWidget(self.setDialogBtn)
        self.box.addWidget(self.getDialogBtn)
        self.box.addWidget(self.infos)

        self.initSetDialog()
        self.initGetDialog()

    def initSetDialog(self):
        self.edits = [] # type: list[QLineEdit]
        texts = [
            "在指定索引处插入项目, (index, item, userData=None)",
            "移除项 (index)"
        ]
        functions = [
            lambda: self.addItem(self.edits[0].text().split(',')),
            lambda: self.comboBox.removeItem(self.toInt(self.edits[1].text()))
        ]

        for t, f in zip(texts, functions):
            title = QLabel(t)
            edit = QLineEdit()
            self.edits.append(edit)
            button = QPushButton("Apply")
            button.clicked.connect(f)
            self.setDialog.box.addWidget(title, alignment=Qt.AlignmentFlag.AlignHCenter)
            self.setDialog.box.addWidget(edit)
            self.setDialog.box.addWidget(button)
        ...

    def initGetDialog(self):
        texts = [
            "获取当前索引",
            "获取当前项",
            "获取当前项的userData",
            "获取项目个数"
        ]
        functions = [
            lambda: self.infos.append(f"当前项索引为: {self.comboBox.currentIndex()}"),
            lambda: self.infos.append(f"当前项为: {self.comboBox.currentText()}"),
            lambda: self.infos.append(f"当前项的userData为: {self.comboBox.itemData(self.comboBox.currentIndex())}"),
            lambda: self.infos.append(f"项目个数为: {self.comboBox.count()}")
        ]
        for t, f in zip(texts, functions):
            title = QLabel(t)
            button = QPushButton("Get")
            button.clicked.connect(f)
            self.getDialog.box.addWidget(title, alignment=Qt.AlignmentFlag.AlignHCenter)
            self.getDialog.box.addWidget(button)


    def addItem(self, args):
        length = len(args)
        index = self.toInt(args[0])
        if length == 3:
            self.comboBox.insertItem(index, args[1], args[2])
            self.infos.append(f"添加成功, index: {index}, item: {args[1]}, userData: {args[2]}")
        elif length == 2:
            self.comboBox.insertItem(self.toInt(args[0]), args[1])
            self.infos.append(f"添加成功, index: {index}, item: {args[1]}, userData: None")
        else:
            self.infos.append("添加失败")

    def toInt(self, item):
            try:
                return int(item)
            except:
                return 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QComboBoxInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
    ...