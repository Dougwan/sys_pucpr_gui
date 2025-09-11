from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt
from typing_extensions import override
from config import PRIMARY_COLOR, PRIMARY_COLOR_DARKER, LIGHT_COLOR

qss_stylesheet = f"""
        QPushButton {{ height: 40px; font-family: Inter; font-size: 16px; border-radius: 8px; color: {PRIMARY_COLOR}; border: 2px solid {PRIMARY_COLOR}; letter-spacing: 0.8px; padding: 10px; }}
        QPushButton::hover {{ background-color: {PRIMARY_COLOR_DARKER}; color: {LIGHT_COLOR}; border: 0px; }}
        QPushButton::pressed {{ background-color: {PRIMARY_COLOR}; color: {LIGHT_COLOR}; border: 0px; }}
        QPushButton::disabled {{background-color: gray; border: 0px; color: {LIGHT_COLOR}; }}
"""


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(qss_stylesheet)

    @override
    def enterEvent(self, event):
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        super().enterEvent(event)

    @override
    def leaveEvent(self, event):
        self.unsetCursor()
        super().leaveEvent(event)
