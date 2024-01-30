import sys
from PyQt6.QtWidgets import QApplication
from app.window import GestXWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GestXWindow()
    window.show()
    window.center()
    app.exec()
