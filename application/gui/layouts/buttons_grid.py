from PySide6.QtWidgets import QGridLayout
from PySide6.QtCore import Qt
from ..widgets.button import Button
from typing import List


class ButtonsGrid(QGridLayout):
    def __init__(self, items=List[List[Button]], *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setAlignment(Qt.AlignmentFlag.AlignBottom)

        self._items = items
        self._set_buttons_in_grid()

    def _get_grid_greater_column_span(self):
        greatest_column_span = 0

        for _, column_data in enumerate(self._items):
            if len(column_data) > greatest_column_span:
                greatest_column_span = len(column_data)

        return greatest_column_span

    def _set_buttons_in_grid(self):
        self._get_grid_greater_column_span()

        for row, row_data in enumerate(self._items):
            for col, button in enumerate(row_data):
                self.addWidget(
                    button,
                    row,
                    col,
                    1,
                    1 if len(row_data) > 1 else self._get_grid_greater_column_span(),
                )
