from .main_window import MainWindow
from ..layouts.buttons_grid import ButtonsGrid


class MainMenu():
    def __init__(self):
        self._actions_mask = [
            ['estudantes', 'diciplinas'],
            ['professores', 'turmas'],
            ['matrículas']
        ]

        self.buttons_grid = ButtonsGrid(self._actions_mask)
