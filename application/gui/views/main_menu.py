from gc import enable
from turtle import title
from typing import Callable, Dict, Union, Iterator

from ..widgets.menu import Menu
from type_defs.menu import MenuOption, MenuOptions
from config import IMAGES_PATH
from PySide6.QtWidgets import QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


def was_entity_enabled(entity: str) -> bool:
    from config import ENABLED_FEATURES

    return ENABLED_FEATURES.get(entity, {}).get("enable", False)


def get_entities() -> Iterator[Dict[str, Union[str, bool]]]:
    entities = [
        {"title": "estudantes", "key": "students"},
        {"title": "diciplinas", "key": "courses"},
        {"title": "professores", "key": "teachers"},
        {"title": "turmas", "key": "classes"},
        {"title": "matrículas", "key": "enrollments"},
    ]

    return map(
        lambda entity: {**entity, "enabled": was_entity_enabled(entity["key"])},
        entities,
    )


class MainMenu(Menu):
    def __init__(self, option_callback: Callable) -> None:
        self._option_callback = option_callback
        super().__init__(self._make_menu_options())

    def _make_menu_options(self) -> MenuOptions:

        options = []

        for entity in get_entities():
            option: MenuOption = {
                "key": str(entity["key"]),
                "title": str(entity["title"]).capitalize(),
                "enable": bool(entity.get("enabled", False)),
                "callback": self._option_callback,
            }

            options.append(option)

        return MenuOptions(options)
