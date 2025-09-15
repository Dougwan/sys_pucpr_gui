from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QPushButton, QSizePolicy
from config import LIGHT_COLOR, PRIMARY_COLOR, PRIMARY_COLOR_DARKER
from functools import partial
from typing import TYPE_CHECKING
from database.database import Database

if TYPE_CHECKING:
    from ..action_view import ActionView

qss_stylesheet = f"""
        QPushButton {{ height: 20px; font-family: Inter; border-radius: 8px; color: {LIGHT_COLOR}; background-color: {PRIMARY_COLOR_DARKER}; letter-spacing: 0.8px; padding: 10px; }}
        QPushButton::hover {{ background-color: {PRIMARY_COLOR};}}
        QPushButton::pressed {{ background-color: {PRIMARY_COLOR_DARKER};}}
"""


class CreateView():
    def __init__(self, parent: "ActionView"):
        self._parent = parent
        self._create_action_widget()
        self._database = Database()

    def _create_student(self, input: QLineEdit) -> None:
        if (input.text() == ""):
            return

        self._database.add_item("students", input.text())
        input.setText("")

    def _create_action_widget(self) -> None:
        input_field = QLineEdit()
        input_field.setPlaceholderText("Digite o nome completo do estudante")
        input_field.setTextMargins(10, 10, 10, 10)
        input_field.setStyleSheet(
            f"background-color: {LIGHT_COLOR}; border-radius: 5px; color: #0f0f0f; font-size: 16px;"
        )

        submit_button = QPushButton("Incuir novo aluno")
        submit_button.setStyleSheet(qss_stylesheet)
        submit_button.setCursor(Qt.CursorShape.PointingHandCursor)
        submit_button.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Fixed)  # type: ignore

        button_slot = partial(
            self._create_student, input_field)

        submit_button.clicked.connect(button_slot)

        self._parent.panel_widget.layout().addWidget(
            input_field, alignment=Qt.AlignmentFlag.AlignTop)  # type: ignore
        self._parent.panel_widget.layout().addWidget(submit_button)  # type: ignore
