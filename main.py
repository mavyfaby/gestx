import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication
from qfluentwidgets import *


class GestX(MSFluentWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitleBar(FluentTitleBar(self))
        self.setWindowTitle("GestX")
        self.setMinimumSize(480, 640)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gestx = GestX()
    gestx.show()
    app.exec()
