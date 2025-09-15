from PySide6.QtWidgets import QVBoxLayout, QWidget, QSizePolicy, QLineEdit, QPushButton
from PySide6.QtCore import Qt

from functools import partial
from typing import TYPE_CHECKING

from ..widgets.button import Button
from type_defs.menu import MenuOption
from config import LIGHT_COLOR, PRIMARY_COLOR, PRIMARY_COLOR_DARKER
from .students.create_view import CreateView as StudentCreateView
from .students.list_view import ListView as StudentListView


if TYPE_CHECKING:
    from ..views.main_window import MainWindow


qss_stylesheet = f"""
        QPushButton {{ height: 20px; font-family: Inter; border-radius: 8px; color: {LIGHT_COLOR}; background-color: {PRIMARY_COLOR_DARKER}; letter-spacing: 0.8px; padding: 10px; }}
        QPushButton::hover {{ background-color: {PRIMARY_COLOR};}}
        QPushButton::pressed {{ background-color: {PRIMARY_COLOR_DARKER};}}
"""


class ActionView(QWidget):
    def __init__(
        self,
        parent: "MainWindow",
        action: MenuOption,
        entity: MenuOption,
    ) -> None:
        super().__init__()

        self._parent = parent
        self._action = action
        self._entity = entity

        self._set_page_layout()
        self._set_page_widgets()
        self.adjustSize()

    def _set_page_layout(self) -> None:
        layout = QVBoxLayout()
        self.setLayout(layout)

    def _set_page_widgets(self) -> None:
        self.panel_widget = self._create_panel_widget()
        self._create_go_to_action_menu_button()

        if self._action["key"] == "create" and self._entity["key"] == 'students':
            StudentCreateView(self)

        if self._action["key"] == "read" and self._entity["key"] == 'students':
            StudentListView(self)

    def _create_panel_widget(self) -> QWidget:
        panel_layout = QVBoxLayout()
        panel_widget = QWidget()

        panel_widget.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)  # type: ignore
        panel_widget.setStyleSheet(
            "background-color: #e8e8e8; border-radius: 8px;")

        panel_widget.setLayout(panel_layout)
        self.layout().addWidget(panel_widget)  # type: ignore

        return panel_widget

    def _create_go_to_action_menu_button(self) -> None:
        button = Button("Voltar ao menu de ações")
        button.setSizePolicy(QSizePolicy.Expanding,
                             QSizePolicy.Fixed)  # type: ignore

        button_slot = partial(
            self._parent.go_to_main_menu, self, self._parent.actions_menu
        )

        button.clicked.connect(button_slot)
        self.layout().addWidget(button)  # type: ignore
