"""
НЕОБЯЗАТЕЛЬНЫЙ МОДУЛЬ  

Модуль не являеться главным в проекте!  
Главная задача модуля это автоматизировать создание некоторых `HTML` элементов.  

По этому этот модуль можно изменять без последствий для проекта, под свой нужды.  
"""

from typing import Any

import os
import pyHTML
htmlElements_dir = os.path.dirname(os.path.abspath(__file__))
"""Полный путь до папки "`htmlElements`", что находится в корневой папке.  """

def init(head:pyHTML.HTMLelement) -> None:
    """
    Устанавливает `CSS` стили в `Head` `HTML` страницы.
    """
    pyHTML.addFileText(head, f"{htmlElements_dir}/global.css", "style")
    pyHTML.addFileText(head, f"{htmlElements_dir}/image.css", "style")

def addFastTag(htmlElement:str, *objects:Any, attributes:dict[str,Any]={}) -> pyHTML.HTMLelement:
    """
    Функция один раз создаёт класс для `HTML` елемента, который больше нигде не будет использоваться.  

    `<str> htmlTag` -- `HTML` елемент который нужно единожды создать.  
    `<any> * objects` -- Массив объектов что нужно увидить в `HTML` элементе.  
    `<str> attributes` -- Атрибуты `HTML` элемента.  
    """
    
    htmlElement = pyHTML.HTMLelement(htmlElement)
    htmlElement.attributes = attributes
    for i in objects:
        htmlElement.append(i)
        
    return htmlElement

from .text import text
from .language import language

__version__ = "0.0.0"
__all__ = [
    "htmlElements_dir",
    
    "init",

    "text",
]
