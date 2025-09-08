from PySide6.QtWidgets import QWidget
from ..layouts.buttons_grid import ButtonsGrid
from ..widgets.button import Button
from typing import List, Callable
from config import PRIMARY_COLOR, PRIMARY_COLOR_DARKER, LIGHT_COLOR
from type_defs.menu import MenuOptions


def create_button_slot(callback: Callable, *args, **kwargs) -> Callable:
    def slot():
        callback(*args, **kwargs)

    return slot


class Menu(QWidget):
    def __init__(
        self,
        options: MenuOptions,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        self._options = options
        self.setLayout(ButtonsGrid(self._make_menu_grid_options()))

        self.setStyleSheet(
            f"""
                  QPushButton {{ font-family: Inter; border-radius: 8px; color: {PRIMARY_COLOR}; border: 2px solid {PRIMARY_COLOR}; letter-spacing: 0.8px; padding: 10px; }}
                  QPushButton::hover {{ background-color: {PRIMARY_COLOR_DARKER}; color: {LIGHT_COLOR}; border: 0px; }}
                  QPushButton::pressed {{ background-color: {PRIMARY_COLOR}; color: {LIGHT_COLOR}; border: 0px; }}
             """
        )

    def _make_menu_grid_options(self, max_columns: int = 2) -> List[List[Button]]:
        grid = []
        menu_options = self._options

        for row in range(0, len(menu_options), max_columns):
            options = menu_options[row : (row + max_columns)]

            buttons = []
            for _, option in enumerate(options):
                button = Button(option["title"].capitalize())
                button_slot = create_button_slot(option["callback"], option)
                button.clicked.connect(button_slot)

                buttons.append(button)

            grid.append(buttons)

        return grid
