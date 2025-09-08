from typing import Callable

from ..widgets.menu import Menu
from type_defs.menu import MenuOption, MenuOptions
from config import IMAGES_PATH
from PySide6.QtWidgets import QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class ActionsMenu(Menu):
    def __init__(self, entity_id: int, go_back: Callable) -> None:
        super().__init__(self._make_menu_options(go_back))
        self.entity_id = entity_id

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

    def _handle_creation_action(self, *args, **kwargs) -> None:
        print('Criar', self.entity_id)

    def _handle_list_action(self, *args, **kwargs) -> None:
        print('Listar', self.entity_id)

    def _handle_update_action(self, *args, **kwargs) -> None:
        print('Atualizar', self.entity_id)

    def _handle_delete_action(self, *args, **kwargs) -> None:
        print('Deletar', self.entity_id)

    def _get_action_handler(self, action: str) -> Callable:
        actions = {
            'incluir': self._handle_creation_action,
            'listar': self._handle_list_action,
            'atualizar': self._handle_update_action,
            'excluir': self._handle_delete_action,
        }

        return actions[action]

    def _make_menu_options(self, go_back: Callable) -> MenuOptions:
        actions = ["incluir", "listar", "atualizar", "excluir"]
        options = []

        for idx, action in enumerate(actions):
            option: MenuOption = {
                "id": idx,
                "title": action.capitalize(),
                "callback": self._get_action_handler(action),
            }

            options.append(option)

        go_back_option: MenuOption = {"id": len(options), "title": "Voltar ao menu principal", "callback": go_back}
        options.append(go_back_option)

        return MenuOptions(options)

