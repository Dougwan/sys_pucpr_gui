from ..widgets.menu import Menu
from PySide6.QtWidgets import QVBoxLayout, QWidget, QSizePolicy, QLineEdit, QLabel
from PySide6.QtCore import Qt
from type_defs.menu import MenuOption, MenuOptions
from typing import Callable
from config import LIGHT_COLOR


class ActionView(Menu):
    def __init__(self, go_to_action_menu: Callable[[], None], action: MenuOption, entity: MenuOption) -> None:
        self._action = action
        self._entity = entity
        self._go_to_action_menu = go_to_action_menu

        super().__init__([self._make_go_to_action_menu_option()])

        self._set_page_layout()

        self.panel_widget = self._set_panel_widget()
        self._create_student_creation_panel()

        self.layout().addLayout(self.buttons_grid)

        self.adjustSize()

    def _set_panel_widget(self) -> QWidget:
        panel_layout = QVBoxLayout()
        panel_widget = QWidget()

        panel_widget.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )

        panel_widget.setStyleSheet(
            "background-color: #e8e8e8; border-radius: 8px;"
        )

        panel_widget.setLayout(panel_layout)
        self.layout().addWidget(panel_widget)

        return panel_widget

    def _create_student_creation_panel(self) -> None:
        name_input = QLineEdit()

        name_input.setPlaceholderText("Informe o nome do estudante")

        name_input.setTextMargins(10, 10, 10, 10)

        name_input.setStyleSheet(f"""
            background-color: {LIGHT_COLOR};
            border-radius: 5px;
            color: #0f0f0f;
            font-size: 16px;
        """)

        self.panel_widget.layout().addWidget(
            name_input, alignment=Qt.AlignmentFlag.AlignTop)

    def _make_go_to_action_menu_option(self) -> MenuOption:
        return {
            "title": "Voltar ao menu de ações",
            "callback": self._go_to_action_menu,
        }

    def _set_page_layout(self) -> None:
        layout = QVBoxLayout()
        self.setLayout(layout)
