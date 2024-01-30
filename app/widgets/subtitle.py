from PyQt6.QtWidgets import QLabel
from qfluentwidgets import BodyLabel


class Subtitle(BodyLabel):
    def __init__(self, text: str):
        super().__init__()
        self.setText(f'<b>{text}</b>')
