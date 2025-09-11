from functools import partial
from typing import TYPE_CHECKING
from ..widgets.menu import Menu
from PySide6.QtWidgets import QVBoxLayout, QWidget, QSizePolicy, QLineEdit
from PySide6.QtCore import Qt
from type_defs.menu import MenuOption, MenuOptions
from config import LIGHT_COLOR

if TYPE_CHECKING:
    from ..views.main_window import MainWindow


class ActionView(Menu):
    def __init__(
        self, parent: "MainWindow", action: MenuOption, entity: MenuOption
    ) -> None:
        self._parent = parent
        self._action = action
        self._entity = entity

        super().__init__(self._make_go_to_action_menu_option())

        self._set_page_layout()

        self.panel_widget = self._set_panel_widget()
        self._create_student_creation_panel()

        self.layout().addLayout(self.buttons_grid)  # type: ignore

        self.adjustSize()

    def _set_panel_widget(self) -> QWidget:
        panel_layout = QVBoxLayout()
        panel_widget = QWidget()

        panel_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # type: ignore

        panel_widget.setStyleSheet("background-color: #e8e8e8; border-radius: 8px;")

        panel_widget.setLayout(panel_layout)
        self.layout().addWidget(panel_widget)  # type: ignore

        return panel_widget

    def _create_student_creation_panel(self) -> None:
        name_input = QLineEdit()

        name_input.setPlaceholderText("Informe o nome do estudante")

        name_input.setTextMargins(10, 10, 10, 10)

        name_input.setStyleSheet(
            f"""
            background-color: {LIGHT_COLOR};
            border-radius: 5px;
            color: #0f0f0f;
            font-size: 16px;
        """
        )

        self.panel_widget.layout().addWidget(name_input, alignment=Qt.AlignmentFlag.AlignTop)  # type: ignore

    def _make_go_to_action_menu_option(self) -> MenuOptions:
        go_back_option: MenuOption = {
            "title": "Voltar ao menu de ações",
            "callback": partial(
                self._parent.go_to_main_menu, self, self._parent.actions_menu
            ),
        }
        return MenuOptions([go_back_option])

    def _set_page_layout(self) -> None:
        layout = QVBoxLayout()
        self.setLayout(layout)
