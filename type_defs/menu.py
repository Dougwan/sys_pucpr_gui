from typing import TypedDict, Callable, Union


class MenuOption(TypedDict):
    key: str
    title: str
    callback: Callable
    enable: bool


MenuOptions = tuple[MenuOption, ...]
