"""

"""

from .htmlElement import HTMLelement

from .html import HTML

from .head import Head
from .body import Body

def addFileText(element:HTMLelement, filePath:str, htmlElement:str | None) -> None:
    """
    Создает отдельный `HTML` элемент и добовляет его в указанный `HTML` элемент.<br>
    Чтобы добавить весь текст из указанного файла в указанный "HTML" элемент, нужно чтобы переменная "`htmlElement`" оставалась пустой.<br>

    `<HTMLelement> element` -- Элемент в который будет добавлен элемент. Или весь текст из указанного файла.<br>
    `<str> filePath` -- Путь до файла, из которого нужно достать весь текст.<br>
    `<str> htmlElement` -- `HTML` элемент что будет создан в месте с текстом из указанного файла.<br>
    * `None` -- Если переменная будет пустая, то весь текст из указанного файла, будет добавлен в переменеую "`element`".<br>
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

#from .htmlHelper import createHTMLfromAttributes
__version__ = "0.0.0"
__all__ = [
    "HTMLelement",
    "HTML",
    "Head",
    "Body",

    "addFileText",
    ]
