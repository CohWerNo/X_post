"""
НЕОБЯЗАТЕЛЬНЫЙ МОДУЛЬ  

Модуль не являеться главным в проекте!  
Главная задача модуля это автоматизировать создание некоторых `HTML` элементов.  

По этому этот модуль можно изменять без последствий для проекта, под свой нужды.  
"""

import os
import pyHTML
htmlElements_dir = os.path.dirname(os.path.abspath(__file__))
"""Полный путь до папки "`htmlElements_dir`", что находится в корневой папке.  """

def init(head:pyHTML.HTMLelement) -> None:
    """
    Устанавливает `CSS` стили в `Head` `HTML` страницы.
    """
    pyHTML.addFileText(head, f"{htmlElements_dir}/global.css", "style")
    pyHTML.addFileText(head, f"{htmlElements_dir}/image.css", "style")

from .text import text

__version__ = "0.0.0"
__all__ = [
    "init",
    "htmlElements_dir",
    "text",
]
