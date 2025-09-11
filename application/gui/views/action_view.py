from PySide6.QtWidgets import QVBoxLayout, QWidget, QSizePolicy, QLineEdit, QPushButton
from PySide6.QtCore import Qt

from functools import partial
from typing import TYPE_CHECKING

from ..widgets.button import Button
from type_defs.menu import MenuOption
from config import LIGHT_COLOR, PRIMARY_COLOR, PRIMARY_COLOR_DARKER

if TYPE_CHECKING:
    from ..views.main_window import MainWindow


qss_stylesheet = f"""
        QPushButton {{ height: 20px; font-family: Inter; border-radius: 8px; color: {LIGHT_COLOR}; background-color: {PRIMARY_COLOR_DARKER}; letter-spacing: 0.8px; padding: 10px; }}
        QPushButton::hover {{ background-color: {PRIMARY_COLOR};}}
        QPushButton::pressed {{ background-color: {PRIMARY_COLOR_DARKER};}}
"""


class ActionView(QWidget):
    def __init__(
        self,
        parent: "MainWindow",
        action: MenuOption,
        entity: MenuOption,
    ) -> None:
        super().__init__()

        self._parent = parent
        self._action = action
        self._entity = entity

        self._set_page_layout()
        self._set_page_widgets()
        self.adjustSize()

    def _set_page_layout(self) -> None:
        layout = QVBoxLayout()
        self.setLayout(layout)

    def _set_page_widgets(self) -> None:
        self.panel_widget = self._create_panel_widget()
        self._create_go_to_action_menu_button()

        if self._action["key"] == "create":
            self._set_create_action_widgets()

    def _create_panel_widget(self) -> QWidget:
        panel_layout = QVBoxLayout()
        panel_widget = QWidget()

        panel_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # type: ignore
        panel_widget.setStyleSheet("background-color: #e8e8e8; border-radius: 8px;")

        panel_widget.setLayout(panel_layout)
        self.layout().addWidget(panel_widget)  # type: ignore

        return panel_widget

    def _create_go_to_action_menu_button(self) -> None:
        button = Button("Voltar ao menu de ações")
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # type: ignore

        button_slot = partial(
            self._parent.go_to_main_menu, self, self._parent.actions_menu
        )

        button.clicked.connect(button_slot)
        self.layout().addWidget(button)  # type: ignore

    def _set_create_action_widgets(self) -> None:
        input_field = QLineEdit()
        input_field.setPlaceholderText("Digite o nome completo do estudante")
        input_field.setTextMargins(10, 10, 10, 10)
        input_field.setStyleSheet(
            f"background-color: {LIGHT_COLOR}; border-radius: 5px; color: #0f0f0f; font-size: 16px;"
        )

        submit_button = QPushButton("Incuir novo aluno")
        submit_button.setStyleSheet(qss_stylesheet)
        submit_button.setCursor(Qt.CursorShape.PointingHandCursor)
        submit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # type: ignore

        self.panel_widget.layout().addWidget(input_field, alignment=Qt.AlignmentFlag.AlignTop)  # type: ignore
        self.panel_widget.layout().addWidget(submit_button)  # type: ignore
