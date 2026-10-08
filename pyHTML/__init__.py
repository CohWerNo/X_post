"""
Небольшой модуль для быстрого создания `HTML` сайта.
"""


from .htmlElement import HTMLelement

from .html import HTML

from .head import Head
from .body import Body

def addFileText(element:HTMLelement, filePath:str, htmlElement:str | None) -> None:
    """
    Создает отдельный `HTML` элемент и добовляет его в указанный `HTML` элемент.  
    Чтобы добавить весь текст из указанного файла в указанный "HTML" элемент, нужно чтобы переменная "`htmlElement`" оставалась пустой.  

    `<HTMLelement> element` -- Элемент в который будет добавлен элемент. Или весь текст из указанного файла.  
    `<str> filePath` -- Путь до файла, из которого нужно достать весь текст.  
    `<str> htmlElement` -- `HTML` элемент что будет создан в месте с текстом из указанного файла.  
    * `None` -- Если переменная будет пустая, то весь текст из указанного файла, будет добавлен в переменеую "`element`".  
    """

    link:HTMLelement
    if htmlElement:
        link = HTMLelement(htmlElement)
    else:
        link = element

    with open(filePath, "r", encoding="utf-8") as f:
        link.childrens.append(f.read())

    if htmlElement:
        element.childrens.append(link)


__version__ = "1.0.0"
__all__ = [
    "HTMLelement",
    "HTML",
    "Head",
    "Body",

    "addFileText",
]