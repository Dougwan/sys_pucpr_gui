from config import APP_NAME, WINDOW_WIDTH, WINDOW_HEIGHT
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout, QApplication, QLabel

class MainWindow(QMainWindow):
    def __init__(self, application: QApplication) -> None:
        super().__init__()
        self._setup_window(application)

    def _setup_window(self, application: QApplication) -> None:
        self._setup_window_layout()
        self._setup_window_geometry(application)
        self._setup_layout_image()

        self.setWindowTitle(APP_NAME)
        self.setStyleSheet("background-color: #F8F9FA; color: #8A0538")

    def _setup_layout_image(self):
        label = QLabel(self)
        pixmap = QPixmap("assets/images/icon.png")

        label.setPixmap(pixmap)
        label.setFixedSize(320, 130)
        self.window_layout.addWidget(label, 0, 0, alignment=Qt.AlignCenter | Qt.AlignTop)

    def _setup_window_layout(self):
        self.window = QMainWindow()
        self.central_widget = QWidget()
        self.window_layout = QGridLayout()
        self.central_widget.setLayout(self.window_layout)
        self.setCentralWidget(self.central_widget)


    def _setup_window_geometry(self, application: QApplication) -> None:
        screen = application.primaryScreen()
        geometry = screen.availableGeometry()

        pos_x = int((geometry.width() / 2) - (WINDOW_WIDTH / 2))
        pos_y = int((geometry.height() / 2) - (WINDOW_HEIGHT / 2))

        self.setGeometry(pos_x, pos_y, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
