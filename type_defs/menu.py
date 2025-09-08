from typing import TypedDict, Callable


class MenuOption(TypedDict):
    id: int
    title: str
    callback: Callable


MenuOptions = tuple[MenuOption, ...]
