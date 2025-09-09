from typing import Callable

from ..widgets.menu import Menu
from type_defs.menu import MenuOption, MenuOptions
from config import IMAGES_PATH
from PySide6.QtWidgets import QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class ActionsMenu(Menu):
    def __init__(self, go_back: Callable, option_callback: Callable) -> None:
        self._go_back = go_back
        self._option_callback = option_callback

        super().__init__(self._make_menu_options())

        self._set_page_layout()
        self._set_page_icon()
        self.layout().addLayout(self.buttons_grid)

    def _set_page_layout(self) -> None:
        layout = QVBoxLayout()
        self.setLayout(layout)

    def _set_page_icon(self) -> None:
        pixmap = QPixmap(IMAGES_PATH / "icon.png")
        label = QLabel()
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout().addWidget(label)

    def _make_menu_options(self) -> MenuOptions:
        actions = ["incluir", "listar", "atualizar", "excluir"]
        options = []

        for idx, action in enumerate(actions):
            option: MenuOption = {
                "id": idx,
                "title": action.capitalize(),
                "callback": self._option_callback,
            }

            options.append(option)

        go_back_option: MenuOption = {
            "id": len(options),
            "title": "Voltar ao menu principal",
            "callback": self._go_back,
        }

        options.append(go_back_option)

        return MenuOptions(options)
