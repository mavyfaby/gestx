from PyQt6.QtGui import QIcon
from qfluentwidgets import *
from qfluentwidgets import FluentIcon as FIF
from app.views.home import HomeView


class GestXWindow(MSFluentWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitleBar(MSFluentTitleBar(self))
        self.setWindowTitle("GestX")
        self.setMinimumSize(480, 640)
        self.setWindowIcon(QIcon("assets/gestx_white.png"))
        setThemeColor(QColor("#106EBE"))

        self.addSubInterface(HomeView(self), FIF.HOME, "Home")

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
