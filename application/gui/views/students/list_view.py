from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidget, QSizePolicy, QListWidgetItem, QLabel
from typing import TYPE_CHECKING
from database.database import Database
from config import PRIMARY_COLOR

if TYPE_CHECKING:
    from ..action_view import ActionView


class ListView():
    def __init__(self, parent: "ActionView"):
        self._parent = parent
        self._database = Database()
        self._create_list_widget()

    def _create_list_widget(self) -> None:
        if len(self._database.get_item('students')) == 0:
            label = QLabel("Nenhum estudante cadastrado")
            label.setStyleSheet(
                f"color: {PRIMARY_COLOR}; font-size: 16px; font-weight: bold;"
            )
            self._parent.panel_widget.layout().addWidget(
                label, alignment=Qt.AlignmentFlag.AlignCenter
            )

            return

        list_widget = QListWidget()

        for row in self._database.get_item("students"):
            item = QListWidgetItem(row)
            list_widget.addItem(item)

        list_widget.setStyleSheet(
            f"""QListWidget {{
                padding: 5px;
                font-size: 16px;
            }}

            QListWidget::item {{
                color: {PRIMARY_COLOR};
                border-radius: 6px;
                padding: 10px;
                background-color: #fff;
                margin-bottom: 5px;
            }}""")

        list_widget.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Fixed)

        self._parent.panel_widget.layout().addWidget(
            list_widget, alignment=Qt.AlignmentFlag.AlignTop
        )
