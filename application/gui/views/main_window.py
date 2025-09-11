from PySide6.QtWidgets import QMainWindow, QStackedWidget, QApplication, QWidget

from typing import Optional
from .main_menu import MainMenu
from .actions_menu import ActionsMenu
from .action_view import ActionView
from type_defs.menu import MenuOption
from config import APP_NAME, WINDOW_WIDTH, WINDOW_HEIGHT, LIGHT_COLOR


class MainWindow(QMainWindow):
    def __init__(self, application: QApplication, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._setup_window(application)
        self._render_main_menu()

    def _setup_window(self, application: QApplication) -> None:
        self._set_window_title("Menu Principal")
        self._setup_window_geometry(application)
        self._setup_window_widget()

        self.setStyleSheet(f"background-color:{LIGHT_COLOR}; font-family:Inter;")

    def _setup_window_widget(self):
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

    def _setup_window_geometry(self, application: QApplication) -> None:
        screen = application.primaryScreen()
        geometry = screen.availableGeometry()

        pos_x = int((geometry.width() / 2) - (WINDOW_WIDTH / 2))
        pos_y = int((geometry.height() / 2) - (WINDOW_HEIGHT / 2))

        self.setGeometry(pos_x, pos_y, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

    def _set_window_title(self, title: Optional[str] = None) -> None:
        self.setWindowTitle(f"{APP_NAME} - {title}" if title else APP_NAME)

    def _set_previous_window_title(self):
        current_window_title = self.windowTitle()
        splitted_title = current_window_title.split(" - ")

        splitted_title.pop()
        splitted_title.pop(0)

        if len(splitted_title) > 0:
            return " - ".join(splitted_title)

        return "Menu Principal"

    def go_to_main_menu(
        self, current_widget: QWidget, previous_widget: QWidget, *args, **kwargs
    ) -> None:

        self._set_window_title(self._set_previous_window_title())

        self.stack.setCurrentWidget(previous_widget)
        self.stack.removeWidget(current_widget)
        current_widget.deleteLater()

    def _render_main_menu(self) -> None:
        self.main_menu = MainMenu(self._render_actions_view)

        self.stack.addWidget(self.main_menu)
        self.stack.setCurrentWidget(self.main_menu)

    def _render_actions_view(self, option: MenuOption) -> None:

        self._set_window_title(option["title"].capitalize())

        self.actions_menu = ActionsMenu(
            parent=self,
            entity=option,
            action_callback=self._render_action_view,
        )

        self.stack.addWidget(self.actions_menu)
        self.stack.setCurrentWidget(self.actions_menu)

    def _render_action_view(
        self,
        entity: MenuOption,
        action: MenuOption,
    ) -> None:
        self._set_window_title(
            f"{entity['title'].capitalize()} - {action['title'].capitalize()}"
        )
        self.action_view = ActionView(self, action, entity)

        self.stack.addWidget(self.action_view)
        self.stack.setCurrentWidget(self.action_view)
