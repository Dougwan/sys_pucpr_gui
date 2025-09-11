from functools import partial
from ..widgets.menu import Menu
from type_defs.menu import MenuOption, MenuOptions
from typing import TYPE_CHECKING, Callable, Dict, Iterator, Union

if TYPE_CHECKING:
    from ..views.main_window import MainWindow


def was_action_enabled(entity: str, action_key: str) -> bool:
    from config import ENABLED_FEATURES

    return ENABLED_FEATURES.get(entity, {}).get("actions", {}).get(action_key, False)


def get_actions(entity: str) -> Iterator[Dict[str, Union[str, bool]]]:
    all_actions = [
        {"title": "incluir", "key": "create"},
        {"title": "listar", "key": "read"},
        {"title": "atualizar", "key": "update"},
        {"title": "excluir", "key": "delete"},
    ]

    return map(
        lambda action: {**action, "enabled": was_action_enabled(entity, action["key"])},
        all_actions,
    )


class ActionsMenu(Menu):
    def __init__(
        self,
        parent: "MainWindow",
        entity: MenuOption,
        action_callback: Callable[[MenuOption, MenuOption], None],
    ) -> None:
        self._parent = parent
        self._entity = entity
        self._action_callback = action_callback

        super().__init__(self._make_menu_options())

    def _make_menu_options(self) -> MenuOptions:
        options = []

        for action in get_actions(self._entity["key"]):
            option: MenuOption = {
                "key": str(action["key"]),
                "enable": bool(action.get("enabled", False)),
                "title": str(action["title"]).capitalize(),
                "callback": partial(self._action_callback, self._entity),
            }

            options.append(option)

        go_back_option: MenuOption = {
            "enable": True,
            "key": "go_back",
            "title": "Voltar ao menu principal",
            "callback": partial(
                self._parent.go_to_main_menu, self, self._parent.main_menu
            ),
        }

        options.append(go_back_option)

        return MenuOptions(options)
