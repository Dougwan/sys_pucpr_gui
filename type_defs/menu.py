from typing import TypedDict, Callable


class MenuOption(TypedDict):
    title: str
    callback: Callable


MenuOptions = tuple[MenuOption, ...]
