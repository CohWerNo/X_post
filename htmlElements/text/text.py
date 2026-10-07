"""

"""

import pyHTML

import os
cssPath = os.path.dirname(os.path.abspath(__file__))

def init(head:pyHTML.HTMLelement):
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

    """
    def __init__(self):
        """

        """

        super().__init__("text")

class TextMonospace (Default):
    """

    """
    def __init__(self):
        """

        """

        super().__init__("text_monospace")

__versin__ = "0.0.0"
__all__ = [
    "init",
    "Text",
    "TextMonospace",
    ]
