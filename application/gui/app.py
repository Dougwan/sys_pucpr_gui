import sys
from PySide6.QtWidgets import QApplication
from .main_window import MainWindow

def run_app():
    app = QApplication(sys.argv)
    main_window = MainWindow(application=app)

    main_window.show()
    sys.exit(app.exec())

