from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListView, QSizePolicy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..action_view import ActionView


class ListView():
    def __init__(self, parent: "ActionView"):
        self._parent = parent
        self._create_list_widget()

    def _create_list_widget(self) -> None:
        list_widget = QListView()

        for row in self._parent.database:
            list_widget.addItem(row)

        list_widget.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Fixed)

        self._parent.panel_widget.layout().addWidget(
            list_widget, alignment=Qt.AlignmentFlag.AlignTop
        )
