from typing import Callable

from ..widgets.menu import Menu
from type_defs.menu import MenuOption, MenuOptions
from config import IMAGES_PATH
from PySide6.QtWidgets import QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class ActionsMenu(Menu):
    def __init__(self, go_to_main_menu: Callable[[], None], action_callback: Callable[[MenuOption, MenuOption], None], entity: MenuOption) -> None:
        self._entity = entity
        self._got_to_main_menu = go_to_main_menu
        self._action_callback = action_callback

        super().__init__(self._make_menu_options())

        self._set_page_layout()
        self._set_page_icon()
        self.layout().addLayout(self.buttons_grid)

    def _make_menu_options(self) -> MenuOptions:
        actions = ["incluir", "listar", "atualizar", "excluir"]
        options = []

        def action_callback(option: MenuOption): return self._action_callback(
            option, self._entity)

        for _, action in enumerate(actions):
            option: MenuOption = {
                "title": action.capitalize(),
                "callback": action_callback,
            }

            options.append(option)

        go_back_option: MenuOption = {
            "title": "Voltar ao menu principal",
            "callback": self._got_to_main_menu,
        }

        options.append(go_back_option)

        return MenuOptions(options)

    def _set_page_layout(self) -> None:
        layout = QVBoxLayout()
        self.setLayout(layout)

    def _set_page_icon(self) -> None:
        pixmap = QPixmap(IMAGES_PATH / "icon.png")
        label = QLabel()
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout().addWidget(label)
