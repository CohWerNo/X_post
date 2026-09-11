import pyHTML

class Default (pyHTML.HTMLelement):
    """
    Класс с настройками по умолчанию.
    """
    def __init__(self, htmlElement:str):
        """
        Создает класс с настройками по умолчанию.

        <str> htmlElement -- `HTML` элемент.
        """

        cssPath = ""

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
