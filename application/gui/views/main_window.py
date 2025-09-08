from typing import Optional
from config import APP_NAME, WINDOW_WIDTH, WINDOW_HEIGHT, IMAGES_PATH, LIGHT_COLOR
from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QApplication,
    QWidget
)

from .main_menu import MainMenu
from .actions_menu import ActionsMenu
from type_defs.menu import MenuOption


class MainWindow(QMainWindow):
    def __init__(self, application: QApplication, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.main_menu = None
        self.actions_menu = None

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

    def _render_main_menu(self) -> None:
        self.main_menu = MainMenu(self._render_option_actions_page)
        self.stack.addWidget(self.main_menu)

    def _go_to_main_menu(self, current_page: QWidget) -> None:
        self._set_window_title("Menu Principal")
        self.stack.setCurrentWidget(self.main_menu)
        self.stack.removeWidget(current_page)
        current_page.deleteLater()

    def _render_option_actions_page(self, selected_option: MenuOption) -> None:
        self._set_window_title(selected_option["title"].capitalize())
        self.actions_menu = ActionsMenu(selected_option['id'], lambda *args: self._go_to_main_menu(self.actions_menu))
        self.stack.addWidget(self.actions_menu)
        self.stack.setCurrentWidget(self.actions_menu)
