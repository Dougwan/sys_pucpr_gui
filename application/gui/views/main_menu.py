from typing import Callable

from ..widgets.menu import Menu
from type_defs.menu import MenuOption, MenuOptions
from config import IMAGES_PATH
from PySide6.QtWidgets import QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class MainMenu(Menu):
    def __init__(self, option_callback: Callable) -> None:
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
        entities = ["estudantes", "diciplinas",
                    "professores", "turmas", "matrículas"]

        options = []

        for _, entity in enumerate(entities):
            option: MenuOption = {
                "title": entity.capitalize(),
                "callback": self._option_callback,
            }

            options.append(option)

        return MenuOptions(options)
