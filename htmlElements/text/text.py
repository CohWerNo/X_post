"""
Текст что обычно будет на сайте.  
Модуль нужен только для удобства разделенния обычного текста, от других элементов.  

Чтобы модуль правильно отображался на сайте, нужно запустить "`init()`".  
"""

import pyHTML

import os
text_dir = os.path.dirname(os.path.abspath(__file__))
"""Полный путь до папки "`text`", что находится в "htmlElements".  """

HTML__TEXT = "text"
"""Это текст для вставки соответствующего `HTML` элкмента.  """
HTML__TEXT_MONOSPACE = "text_monospace"
"""Это текст для вставки соответствующего `HTML` элкмента.  """

def init(head:pyHTML.HTMLelement):
    """
    Устанавливает `CSS` стили в `Head` `HTML` страницы.
    """
    pyHTML.addFileText(head, f"{text_dir}/text.css", "style")

class _Default (pyHTML.HTMLelement):
    """
    Класс с настройками по умолчанию.  
    """
    def __init__(self, htmlElement:str):
        """
        Создает класс с настройками по умолчанию.  

        <str> htmlElement -- `HTML` элемент.  
        """

        super().__init__(htmlElement)

class Text (_Default):
    """
    Стандартный текст что в основном и будет находится на сайте.  
    Нужно это для удобного разделения текстовых элементов от других элементов.  
    """
    def __init__(self):
        """
        Создаёт текстовый `HTML` элемент.  
        """

        super().__init__(HTML__TEXT)

class TextMonospace (_Default):
    """
    Это тоже текст но моноширный, то есть текст будет занимать указанную область всегда.  
    """
    def __init__(self):
        """
        Создаёт моноширно текстовый `HTML` элемент.  
        """

        super().__init__(HTML__TEXT_MONOSPACE)

__versin__ = "1.0.0"
__all__ = [
    "init",

    "Text",
    "TextMonospace",
]
