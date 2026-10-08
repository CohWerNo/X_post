"""
Текст что обычно будет на сайте.  
Модуль нужен только для удобства разделенния обычного текста, от других элементов.  
"""

import pyHTML

import os
cssPath = os.path.dirname(os.path.abspath(__file__))

def init(head:pyHTML.HTMLelement):
    """
    Устанавливает `CSS` стили в `Head` `HTML` страницы.
    """
    pyHTML.addFileText(head, f"{cssPath}/text.css", "style")

class Default (pyHTML.HTMLelement):
    """
    Класс с настройками по умолчанию.  
    """
    def __init__(self, htmlElement:str):
        """
        Создает класс с настройками по умолчанию.  

        <str> htmlElement -- `HTML` элемент.  
        """

        super().__init__(htmlElement)

class Text (Default):
    """
    Стандартный текст что в основном и будет находится на сайте.  
    Нужно это для удобного разделения текстовых элементов от других элементов.  
    """
    def __init__(self):
        """
        Создаёт текстовый `HTML` элемент.  
        """

        super().__init__("text")

class TextMonospace (Default):
    """
    Это тоже текст но моноширный, то есть текст будет занимать указанную область всегда.  
    """
    def __init__(self):
        """
        Создаёт моноширно текстовый `HTML` элемент.  
        """

        super().__init__("text_monospace")

__versin__ = "0.0.0"
__all__ = [
    "init",
    "Text",
    "TextMonospace",
]
