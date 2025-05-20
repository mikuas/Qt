import sys
from typing import overload

from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLineEdit, QDialog, QLabel
from PySide6.QtCore import QPoint, QPointF, QPropertyAnimation, QUrl

# from Interface import WidgetInterface
from .Interface import WidgetInterface


class Point(QPoint):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, xpos: int, ypos: int): # QPointF: Args: xpos: float, ypos: float
        """_summary_

        Args:
            xpos (int | float): x轴位置
            ypos (int | float): y轴位置
        """
        ...


class Function(Point):
    
    # 设置x坐标
    def setX(self, x: int | float) -> None:
        super().setX(x)
    
    # 设置y坐标
    def setY(self, y: int | float) -> None:
        super().setY(y)
    
    def x(self):
        return super().x()

    def y(self):
        return super().y()

    # 将 x 和 y 对掉
    def transposed(self):
        return super().transposed()

    def toTuple(self) -> tuple[x, y]:
        return super().toTuple()


class QPointInterface(WidgetInterface):
    def __init__(self, parent=None):
        super().__init__(parent, True, True, True)
        self.edit.setPlaceholderText("设置移动的QPoint, 用逗号隔开(x,y), 不写默认为0")
        
        self.moveBtn = QPushButton("MOVE BUTTON", self)
        self.moveBtn.setMinimumSize(100, 100)
        self.moveBtn.setStyleSheet("background: deeppink;")
        self.moveBtn.move(150, 150)
        
        self.button.setText("MOVE")
        self.button.clicked.connect(lambda: self.createPosAni(self.getPos()))
        
        self.box.addWidget(self.edit)
        self.box.addWidget(self.button)
        self.box.addWidget(self.getDialogBtn)
        self.box.addWidget(self.setDialogBtn)
        self.box.addWidget(self.infos)
        
        self.posAni = QPropertyAnimation(self.moveBtn, b'pos', self)
        
        self.initGetDialog()
        self.initSetDialog()

    def initGetDialog(self): 
        texts = [
            "获取X轴坐标",
            "获取Y轴坐标",
            "获取X和Y是否为空(x=y=0)"
        ]
        functions = [
            lambda: {
                self.infos.append(f"X轴坐标: {self.moveBtn.pos().x()}")
            },
            lambda: {
                self.infos.append(f"YA轴坐标: {self.moveBtn.pos().y()}")
            },
            lambda: {
                self.infos.append("X和Y为空" if self.moveBtn.pos().isNull() else "X和Y不为空")
            }
        ]
        
        for text, function in zip(texts, functions):
            hBox = QHBoxLayout()
            self.getDialog.box.addLayout(hBox)
            hBox.addWidget(QLabel(text))
            button = QPushButton(text[:2])
            button.clicked.connect(function)
            hBox.addWidget(button)
        
    def initSetDialog(self):
        hBox = QHBoxLayout()
        self.setDialog.box.addLayout(hBox)
        hBox.addWidget(QLabel("对调X和Y轴"))
        button = QPushButton("对调")
        button.clicked.connect(lambda: {
            self.createPosAni(self.moveBtn.pos().transposed().toTuple()),
            self.infos.append(f"已对调X和Y轴, 结果为: X: {self.moveBtn.pos().x()} | Y: {self.moveBtn.pos().y()}")
        })
        hBox.addWidget(button)

    def createPosAni(self, targetPos):
        self.posAni.setDuration(1000)
        self.posAni.setStartValue(self.moveBtn.pos())
        currentPos = self.moveBtn.pos().toTuple()
        self.infos.append(f"按钮从 X: {currentPos[0]} | Y: {currentPos[1]} 移动到了 X: {targetPos[0]} | Y {targetPos[1]}")
        self.posAni.setEndValue(QPoint(*targetPos))
        self.posAni.start()
    
    def getPos(self):
        point = self.edit.text()
        if point:
            point = point.split(',')
            if len(point) >= 2:
                return [self.verify(point[0]), self.verify(point[1])]
            else:
                return [self.verify(point[0]), 0]
        return [0, 0]
    
    def verify(self, point):
        try:
            return int(point)
        except ValueError:
            return 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QPointInterface()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())
    ...