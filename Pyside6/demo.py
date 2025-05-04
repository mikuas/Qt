from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QAbstractButton, QPushButton, QButtonGroup
from PySide6.QtCore import QTimer, QTime

from pmutils import KeyboardUtils

ku = KeyboardUtils()

app = QApplication([])

time = QTime()

timer = QTimer()
timer.timeout.connect(lambda: run(23, 42))

def run(H: int, M: int):
    h_m = getH_M()
    h = h_m[0]
    m = h_m[1]
    if h == H and m == M:
        ku.Hotkey('ctrl,alt,space')
        timer.stop()
        app.exit()

def getH_M():
    h_m = time.currentTime().toString().split(":")[:2]
    return [int(_) for _ in h_m]

timer.start(1000)

app.exec()