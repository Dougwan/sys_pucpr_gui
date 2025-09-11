from PySide6.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from typing import List
from functools import partial

from type_defs.menu import MenuOptions
from config import IMAGES_PATH

from ..layouts.buttons_grid import ButtonsGrid
from ..widgets.button import Button


class Menu(QWidget):
    def __init__(self, options: MenuOptions):
        super().__init__()

        self._options = options

        self._set_layout()
        self._set_page_icon()

        self.buttons_grid = ButtonsGrid(self._make_menu_grid_options())
        self.layout().addLayout(self.buttons_grid)  # type: ignore

    def _set_layout(self) -> None:
        layout = QVBoxLayout()
        self.setLayout(layout)

    def _set_page_icon(self) -> None:
        pixmap = QPixmap(IMAGES_PATH / "icon.png")
        label = QLabel()
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout().addWidget(label)  # type: ignore

    def _make_menu_grid_options(self, max_columns: int = 2) -> List[List[Button]]:
        grid = []
        menu_options = self._options

        for row in range(0, len(menu_options), max_columns):
            options = menu_options[row : (row + max_columns)]

            buttons = []

            for option in options:
                button = Button(option["title"].capitalize())
                button.setEnabled(option["enable"])
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # type: ignore
                button_slot = partial(option["callback"], option)

                button.clicked.connect(button_slot)

                buttons.append(button)

            grid.append(buttons)

        return grid
