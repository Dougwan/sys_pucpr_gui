from typing import Callable

from ..widgets.menu import Menu
from type_defs.menu import MenuOption, MenuOptions


class ActionsMenu(Menu):
    def __init__(self, entity_id: int, go_back: Callable) -> None:
        self.entity_id = entity_id
        self.options = self._make_menu_options(go_back)

        super().__init__(self.options)

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

