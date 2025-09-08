from typing import Callable

from ..widgets.menu import Menu
from type_defs.menu import MenuOption, MenuOptions


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
