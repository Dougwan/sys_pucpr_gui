from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt
from typing_extensions import override

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @override
    def enterEvent(self, event):
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        super().enterEvent(event)

    @override
    def leaveEvent(self, event):
        self.unsetCursor()
        super().leaveEvent(event)