from PySide6.QtWidgets import QWidget, QSizePolicy
from ..layouts.buttons_grid import ButtonsGrid
from ..widgets.button import Button
from typing import List, Callable
from config import PRIMARY_COLOR, PRIMARY_COLOR_DARKER, LIGHT_COLOR
from type_defs.menu import MenuOptions, MenuOption
from PySide6.QtCore import Qt
from functools import partial


qss_stylesheet = f"""
        QPushButton {{ height: 40px; font-family: Inter; font-size: 16px; border-radius: 8px; color: {PRIMARY_COLOR}; border: 2px solid {PRIMARY_COLOR}; letter-spacing: 0.8px; padding: 10px; }}
        QPushButton::hover {{ background-color: {PRIMARY_COLOR_DARKER}; color: {LIGHT_COLOR}; border: 0px; }}
        QPushButton::pressed {{ background-color: {PRIMARY_COLOR}; color: {LIGHT_COLOR}; border: 0px; }}
        QPushButton::disabled {{background-color: gray; border: 0px; color: {LIGHT_COLOR}; }}
"""


class Menu(QWidget):
    def __init__(
        self,
        options: MenuOptions,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self._options = options
        self.setStyleSheet(qss_stylesheet)
        self.buttons_grid = ButtonsGrid(self._make_menu_grid_options())
        self.setStyleSheet(qss_stylesheet)

    def _make_menu_grid_options(self, max_columns: int = 2) -> List[List[Button]]:
        grid = []
        menu_options = self._options

        for row in range(0, len(menu_options), max_columns):
            options = menu_options[row: (row + max_columns)]

            buttons = []
            for _, option in enumerate(options):
                button = Button(option["title"].capitalize())
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                button_slot = partial(option["callback"], option)
                button.clicked.connect(button_slot)

                buttons.append(button)

            grid.append(buttons)

        return grid
