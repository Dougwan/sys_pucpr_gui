import sys
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QApplication
from .views.main_window import MainWindow
from config import QSS_STYLESHEET_PATH, FONTS_PATH


def setup_fonts():
    inter_font_path = str(FONTS_PATH / "inter.ttf")
    QFontDatabase.addApplicationFont(inter_font_path)


def run_app():
    app = QApplication(sys.argv)

    setup_fonts()

    main_window = MainWindow(application=app)
    main_window.show()
    sys.exit(app.exec())
