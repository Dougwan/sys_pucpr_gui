from typing import Callable

from ..widgets.menu import Menu
from type_defs.menu import MenuOption, MenuOptions
from config import IMAGES_PATH
from PySide6.QtWidgets import QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

def make_menu_options(option_callback: Callable) -> MenuOptions:
    entities = ["estudantes", "diciplinas", "professores", "turmas", "matrículas"]
    options = []

    for idx, entity in enumerate(entities):
        option: MenuOption = {
            "id": idx,
            "title": entity.capitalize(),
            "callback": option_callback,
        }

        options.append(option)

    return MenuOptions(options)


class MainMenu(Menu):
    def __init__(self, main_window_callback: Callable) -> None:
        self.options = make_menu_options(main_window_callback)

        super().__init__(self.options)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self._set_page_icon()
        self.layout().addLayout(self.buttons_grid)


    def _set_page_icon(self):
        pixmap = QPixmap(IMAGES_PATH / "icon.png")
        label = QLabel()
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout().addWidget(label)
        self.layout().addStretch()