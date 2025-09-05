import sys
from PySide6.QtWidgets import QApplication
from .views.main_window import MainWindow
from .views.main_menu import MainMenu

from .widgets.button import Button


def run_app():
    app = QApplication(sys.argv)
    main_window = MainWindow(application=app)
    main_menu = MainMenu()

    main_window.add_layout(main_menu.buttons_grid)

    main_window.show()
    sys.exit(app.exec())
