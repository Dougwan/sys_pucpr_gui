from config import APP_NAME, WINDOW_WIDTH, WINDOW_HEIGHT, MAIN_STYLE
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication, QLayout


class MainWindow(QMainWindow):
    def __init__(self, application: QApplication, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._setup_window(application)

    def _setup_window(self, application: QApplication) -> None:
        self.setWindowTitle(APP_NAME)
        self._setup_window_layout()
        self._setup_window_geometry(application)
        self._set_main_style()

    def _set_main_style(self):
        self.setStyleSheet(
            f"background-color: {MAIN_STYLE['background-color']}; color: {MAIN_STYLE['color']}")

    def _setup_window_layout(self):
        self.window = QMainWindow()
        self.central_widget = QWidget()
        self.window_layout = QVBoxLayout()
        self.central_widget.setLayout(self.window_layout)
        self.setCentralWidget(self.central_widget)

    def _setup_window_geometry(self, application: QApplication) -> None:
        screen = application.primaryScreen()
        geometry = screen.availableGeometry()

        pos_x = int((geometry.width() / 2) - (WINDOW_WIDTH / 2))
        pos_y = int((geometry.height() / 2) - (WINDOW_HEIGHT / 2))

        self.setGeometry(pos_x, pos_y, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

    def add_widget(self, widget: QWidget, stretch: int = 0, alignment: Qt.AlignmentFlag = Qt.AlignTop | Qt.AlignLeft) -> None:
        self.central_widget.layout().addWidget(widget, stretch, alignment)

    def add_layout(self, layout: QLayout):
        self.central_widget.layout().addLayout(layout)
