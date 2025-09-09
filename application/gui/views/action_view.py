from ..widgets.menu import Menu
from PySide6.QtWidgets import QVBoxLayout
from type_defs.menu import MenuOption, MenuOptions
from typing import Callable


class ActionView(Menu):
    def __init__(self, go_to_action_menu: Callable[[], None], action: MenuOption, entity: MenuOption) -> None:
        self._action = action
        self._entity = entity
        self._go_to_action_menu = go_to_action_menu

        super().__init__([])

        self._set_page_layout()
        self.layout().addLayout(self.buttons_grid)

    def _set_page_layout(self) -> None:
        layout = QVBoxLayout()
        self.setLayout(layout)
