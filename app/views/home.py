from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QVBoxLayout, QWidget, QHBoxLayout
from qfluentwidgets import PushButton, PrimaryPushButton, SubtitleLabel, BodyLabel, HorizontalSeparator

from app.gestx import GestX
from app.widgets.subtitle import Subtitle


class HomeView(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("Home")

        l1 = Subtitle("Gesture Options")
        btn = PrimaryPushButton("Start")
        btn.clicked.connect(self.start_recognition)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.addWidget(l1)
        layout.addWidget(btn)
        self.setLayout(layout)

    def start_recognition(self):
        GestX.start()