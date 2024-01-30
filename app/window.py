from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

from qfluentwidgets import *


class GestXWindow(MSFluentWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitleBar(FluentTitleBar(self))
        self.setWindowTitle("GestX")
        self.setMinimumSize(480, 640)
        self.setWindowIcon(QIcon("assets/gestx_white.png"))

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
