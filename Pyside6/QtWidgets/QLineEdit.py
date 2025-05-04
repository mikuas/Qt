# coding: utf-8

# CUSTOM_QLINE_EDIT

import sys
from typing import overload

from PySide6.QtWidgets import QApplication, QCompleter, QHBoxLayout, QPushButton, QLineEdit, QLabel, QComboBox, QCheckBox, QFrame, QListView, \
    QDialog, QVBoxLayout, QTextEdit, QPlainTextEdit, QPlainTextEdit
from PySide6.QtCore import QPoint, QPointF, QPropertyAnimation, QUrl, Qt, QMargins, QStringListModel
from PySide6.QtGui import QPixmap, QDesktopServices, QValidator

from Interface import WidgetInterface


class QLineEditInterface(WidgetInterface):
    def __init__(self, parent=None):
        super().__init__(parent, True, True, True)

        # 输入格式
        # self.edit.setInputMask('000.000.000.000')

        self.edit.setFixedHeight(35)
        self.edit.setPlaceholderText("设置文本内容")
        
        self.cursorFuncDialog = QDialog(self)
        self.cursorFuncBtn = QPushButton("光标方法")
        self.cursorFuncBtn.clicked.connect(self.cursorFuncDialog.show)
        
        # self.edit.setValidator(QValidator)
        self.completerText = ['home', 'history', 'happy', 'hot', 'head']

        self.completer = QCompleter(self)
        # 设置弹出模式
        self.completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        self.completer.setModel(QStringListModel(self.completerText)),
        self.edit.setCompleter(self.completer)
        
        popup = self.completer.popup() 
        
        popup.setStyleSheet("""
            QListView {
                background-color: #f0f0f0; /* 背景颜色 */
                border-radius: 10px;
                outline: none;
            }
            QListView::item {
                padding: 5px;
                font-size: 14px;
                border-radius: 3px;
            }
            QListView::item:selected {
                background-color: grey; /* 选中项背景 */
                color: white; /* 选中项字体颜色 */
                border: none;
            }
            QListView::item:hover {
                background-color: grey; /* 选中项背景 */
                color: white; /* 选中项字体颜色 */
                border: none;
            }
        """)
        
        # 设置匹配模式
        self.completer.setFilterMode(Qt.MatchFlag.MatchStartsWith) # 匹配开头
        # self.cp.setFilterMode(Qt.MatchFlag.MatchContains) # 匹配任何部分
        # self.cp.setFilterMode(Qt.MatchFlag.MatchEndsWith) # 匹配结尾
        
        self.button.deleteLater()
        
        self.box.addWidget(self.edit)
        self.box.addWidget(self.setDialogBtn)
        self.box.addWidget(self.getDialogBtn)
        self.box.addWidget(self.cursorFuncBtn)
        self.box.addWidget(self.infos)
    
        self.initSetDialog()
        self.initGetDialog()
        self.initCursourFuncDialog()

        # QLineEdit Signal
        self.edit.textChanged.connect(lambda: { # 文本改变信号
            self.infos.append("QLineEdit Text Change Signal Emit")
        })
        self.edit.textEdited.connect(lambda: { # 文本编辑信号 不适用setText方法
            self.infos.append("QLineEdit Text Edited Signal Emit")
        })
        self.edit.cursorPositionChanged.connect(lambda oldPos, newPos: { # 光标位置改变信号
            self.infos.append("QLineEdit Cursor Position Change Signal Emit" + "Pos" + str(newPos) + str(oldPos))
        })
        # Enter信号
        self.edit.returnPressed.connect(lambda: {
            self.infos.append("QLineEdit Enter Signal Emit")
        })
        self.edit.editingFinished.connect(lambda: { # 编辑完成信号 包含回车
            self.infos.append("QLineEdit Editing Finished Signal Emit")
        })

    def initCursourFuncDialog(self):
        self.cursorFuncDialog.setMinimumSize(600, 350)
        self.cursorFuncDialog.box = QVBoxLayout(self.cursorFuncDialog)
        moveLabel = QLabel("光标移动是是否带选中效果")
        selectCheck = QCheckBox()
        hBox = QHBoxLayout()
        
        hBox.addWidget(moveLabel)
        hBox.addWidget(selectCheck)
        hBox.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorFuncDialog.box.addLayout(hBox)
        
        leftMoveEdit = QLineEdit()
        leftMoveEdit.setPlaceholderText("向左移动多少个字符")
        
        rightMoveEdit = QLineEdit()
        rightMoveEdit.setPlaceholderText("向右移动多少个字符")

        edits = [
            leftMoveEdit, rightMoveEdit
        ]
        texts = [
            "Move",
            "Move",
        ]
        
        functions = [
            lambda: {
                self.edit.cursorBackward(selectCheck.isChecked(), self.verify(leftMoveEdit.text())),
                self.infos.append(f"光标向左移动了{self.verify(leftMoveEdit.text())}个字符" + ("并选中了文字" if selectCheck.isChecked() else "未选中文字"))
            },
            lambda: {
                self.edit.cursorForward(selectCheck.isChecked(), self.verify(rightMoveEdit.text())),
                self.infos.append(f"光标向右移动了{self.verify(rightMoveEdit.text())}个字符" + ("并选中了文字" if selectCheck.isChecked() else "未选中文字"))
            }
        ]
        for edit, text, function in zip(edits, texts, functions):
            button = QPushButton(text)
            button.clicked.connect(function)
            self.cursorFuncDialog.box.addWidget(edit)
            self.cursorFuncDialog.box.addWidget(button)
        
        texts = [
            "向左移动一个单词的长度",
            "向右移动一个单词的长度",
            "光标移动至行首",
            "光标移动至行尾",
            "获取光标位置"
        ]
        functions = [
            lambda: {
                self.edit.cursorWordBackward(selectCheck.isChecked()),
                self.infos.append(f"已向左移动一个单词的长度" + "并选中了文字" if selectCheck.isChecked() else "未选中文字")
            },
            lambda: {
                self.edit.cursorWordForward(selectCheck.isChecked()),
                self.infos.append(f"已向右移动一个单词的长度" + "并选中了文字" if selectCheck.isChecked() else "未选中文字")
            },
            lambda: {
                self.edit.home(selectCheck.isChecked()),
                self.infos.append("光标已移动至行首")
            },
            lambda: {
                self.edit.end(selectCheck.isChecked()),
                self.infos.append("光标已移动至行尾")
            },
            lambda: {
                self.infos.append(f"光标位置为: {self.edit.cursorPosition()}")
            }
        ]
        for text, function in zip(texts, functions):
            button = QPushButton(text)
            button.clicked.connect(function)
            self.cursorFuncDialog.box.addWidget(button)
        
        # 获取指定位置处光标位置
        # self.edit.cursorPositionAt()
        
    
    def initSetDialog(self):
        box1 = QHBoxLayout()
        edit1 = QLineEdit()
        edit1.setPlaceholderText('输入要插入的文本')
        button1 = QPushButton("Apply")
        button1.clicked.connect(lambda: {
                self.edit.insert(edit1.text()),
                self.infos.append(f"已在光标处插入文本: {edit1.text()}")
            })
        box1.addWidget(edit1, 1)
        box1.addWidget(button1, 1)
        self.setDialog.box.addLayout(box1)
    
        box2 = QHBoxLayout()    
        edit2 = QLineEdit()
        edit2.setPlaceholderText("设置占位符")
        button2 = QPushButton('Apply')
        button2.clicked.connect(lambda: {
            self.edit.setPlaceholderText(edit2.text()),
            self.infos.append(f"已设置占位符为: {edit2.text()}")
        })
        box2.addWidget(edit2, 1)
        box2.addWidget(button2, 1)
        self.setDialog.box.addLayout(box2)
        
        texts = [
            "设置是否显示清空按钮",
            "设置是否显示外框线",
            "设置是只读模式",
            "设置文本是否可以拖放",
        ]
        functions = [
            lambda b: {
                self.edit.setClearButtonEnabled(b == Qt.CheckState.Checked),
                self.infos.append("显示清空按钮" if b == Qt.CheckState.Checked else "不显示清空按钮")
            },
            lambda b: {
                self.edit.setFrame(b == Qt.CheckState.Checked),
                self.infos.append("显示外框线" if b == Qt.CheckState.Checked else "不显示外框线")
            },
            lambda b: {
                self.edit.setReadOnly(b == Qt.CheckState.Checked),
                self.infos.append("是只读模式" if b == Qt.CheckState.Checked else "不是只读模式")
            },
            lambda b: {
                self.edit.setDragEnabled(b == Qt.CheckState.Checked),
                self.infos.append("可以拖放" if b == Qt.CheckState.Checked else "不可以拖放")
            },
        ]
        for text, function in zip(texts, functions):
            hBox = QHBoxLayout()
            label = QLabel(text)
            checkBox = QCheckBox(self)
            checkBox.setChecked(text == "设置是否显示外框线")
            checkBox.checkStateChanged.connect(function)
            
            hBox.addWidget(label, 1, Qt.AlignmentFlag.AlignHCenter)
            hBox.addWidget(checkBox, 1, Qt.AlignmentFlag.AlignHCenter)
            self.setDialog.box.addLayout(hBox)

        marginsEdit = QLineEdit()
        marginsEdit.setFixedHeight(35)
        marginsEdit.setPlaceholderText("设置文本区域到外框的距离(left,top,right,bottm)不写默认为0")
        marginsEdit.textChanged.connect(lambda text: {
            self.edit.setTextMargins(self.getMargins(text)),
            self.infos.append(f"已设置文本到外框的距离: left: {self.edit.textMargins().left()}, top: {self.edit.textMargins().top()}, right: {self.edit.textMargins().right()}, bottom: {self.edit.textMargins().bottom()}")
        })
        self.setDialog.box.addWidget(marginsEdit)
        
        texts = [
            "默认值",
            "不显示任何输入,文字内容和个数都不可见",
            "不显示输入的字符,但是显示字符个数",
            "编辑的时候显示字符,不编辑的时候显示掩码"
        ]
        modes = [
            QLineEdit.EchoMode.Normal,
            QLineEdit.EchoMode.NoEcho,
            QLineEdit.EchoMode.Password,
            QLineEdit.EchoMode.PasswordEchoOnEdit,
        ]
        displayModeLable = QLabel("设置显示模式")
        displayModeComboBox = QComboBox()
        displayModeComboBox.setStyleSheet(
            """
            QComboBox::item {
                height: 35px;
                padding: 5px;
                font-size: 14px;
                border-radius: 3px;
            }
            QComboBox::item:selected {
                background: deeppink;
            }
            """
        )
        displayModeComboBox.setFixedHeight(35)
        displayModeComboBox.currentIndexChanged.connect(lambda index: {
            self.edit.setEchoMode(modes[index]),
            self.infos.append(f"已设置显示模式为: {texts[index]}")
        })
        displayModeComboBox.addItems(texts)
        self.setDialog.box.addWidget(displayModeLable)
        self.setDialog.box.addWidget(displayModeComboBox)
        
        completerLabel = QLabel(f"设置补全内容, 用空格隔开, 默认为补全内容为: {self.completerText}")
        completerEdit = QLineEdit()
        completerEdit.setFixedHeight(35)
        # 补全 QCompleter | QStringListModel
        # ecl.textChanged.connect(lambda t: self.edit.setCompleter(t.split(',')))
        completerEdit.textChanged.connect(lambda text: {
            self.completer.setModel(QStringListModel(text.split(' ') + self.completerText)),
            self.edit.setCompleter(self.completer),
            self.infos.append(f'已设置补全内容: {text.split(' ')}')
        })
        self.setDialog.box.addWidget(completerLabel)
        self.setDialog.box.addWidget(completerEdit)
        
    def initGetDialog(self):
        texts = [
            "获取真实文本,而不是显示文本",
            "获取占位符",
        ]
        functions = [
            lambda: {
                self.infos.append(f"显示的文本是: {self.edit.displayText()}")
            },
            lambda: {
                self.infos.append(f"占位符为: {self.edit.placeholderText()}")
            }
        ]
        for text, function in zip(texts, functions):
            hBox = QHBoxLayout()
            label = QLabel(text)
            button = QPushButton(text[:2])
            button.clicked.connect(function)
            
            hBox.addWidget(label)
            hBox.addWidget(button)
            self.getDialog.box.addLayout(hBox)
        
        selectEdit = QLineEdit()
        selectEdit.setPlaceholderText("选择指定范围内的文本(例如0-9, 从0开始,选择9位), 写一位默认选择到结尾")
        selectEdit.setFixedHeight(35)
        selectButton = QPushButton("选择")
        selectButton.clicked.connect(lambda: {
            self.edit.setSelection(*self.verifySelect(selectEdit)),
            self.infos.append(f"已选择{self.verifySelect(selectEdit)}范围的文本, 文本为: {self.edit.selectedText()}")
        })
        self.getDialog.box.addWidget(selectEdit)
        self.getDialog.box.addWidget(selectButton)
        
        selectAllButton = QPushButton("选择全部文本")
        selectAllButton.clicked.connect(lambda: {
            self.edit.selectAll(),
            self.infos.append(f"已选择全部文本: {self.edit.selectedText()}")
        })
        self.getDialog.box.addWidget(selectAllButton)
        
        cancelSelectButton = QPushButton("取消选择")
        cancelSelectButton.clicked.connect(lambda: {
            self.infos.append(f"已取消选择的文本: {self.edit.selectedText()}"),
            self.edit.deselect()
        })
        self.getDialog.box.addWidget(cancelSelectButton)
        
        getHasSelectButton = QPushButton("获取是否有选择的文本")
        getHasSelectButton.clicked.connect(lambda: {
            self.infos.append(f"{f"有, 文本为: {self.edit.selectedText()}" if self.edit.hasSelectedText() else "无"}")
        })
        self.getDialog.box.addWidget(getHasSelectButton)
        
        selectLengthButton = QPushButton("获取选择文本的长度")
        selectLengthButton.clicked.connect(lambda: {
            self.infos.append(f"选择的文本为: {self.edit.selectedText()}, 长度为: {len(self.edit.selectedText())}" if self.edit.hasSelectedText() else "无选择的文本")
        })
        self.getDialog.box.addWidget(selectLengthButton)
        
        getSelectStart = QPushButton("获取选择文本的起始位置")
        getSelectStart.clicked.connect(lambda: {
            self.infos.append(f"选择文本的起始位置为: {self.edit.selectionStart()}" if self.edit.hasSelectedText() else "无选择的文本")
        })
        self.getDialog.box.addWidget(getSelectStart)
        
        getSelectEnd = QPushButton("获取选择文本的终止位置")
        getSelectEnd.clicked.connect(lambda: {
            self.infos.append(f"选择文本的起结束置为: {self.edit.selectionEnd()}" if self.edit.hasSelectedText() else "无选择的文本")
        })
        self.getDialog.box.addWidget(getSelectEnd)
        
        getSelectTextButton = QPushButton("获取选择的文本")
        getSelectTextButton.clicked.connect(lambda: {
            self.infos.append(f"选择的文本为: {self.edit.selectedText()}" if self.edit.hasSelectedText() else "无选择的文本")
        })
        self.getDialog.box.addWidget(getSelectTextButton)
    
    
    def verifySelect(self, obj):
        text = obj.text()
        isNull = bool(self.edit.text())
        if text:
            text = text.split('-')
            if len(text) >= 2 and isNull:
                return [self.verify(text[0]), self.verify(text[1])]
            elif len(text) == 1 and isNull:
                return [self.verify(text[0]), len(self.edit.text())]
        return [0, 0]
    
    def getMargins(self, text):
        if text:
            text = text.split(',')
            margins = []
            for _ in range(4):
                try:
                    margins.append(self.verify(text[_]))
                except IndexError:
                    margins.append(0)
            return QMargins(*margins)
        return QMargins(0, 0, 0, 0)
    
    def verify(self, text):
        try:
            return int(text)
        except ValueError:
            return 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QLineEditInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
    ...