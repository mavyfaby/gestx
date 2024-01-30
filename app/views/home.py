from PyQt6.QtWidgets import QFrame, QVBoxLayout
from qfluentwidgets import PushButton, PrimaryPushButton


class HomeView(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("Home")

        btn = PrimaryPushButton("Start")

        layout = QVBoxLayout()
        layout.addWidget(btn)
        self.setLayout(layout)
