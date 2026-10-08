"""
Тело, это основное место интерфейса и управление `HTML` сайтом через `UI` элементы.  
"""

from .htmlElement import HTMLelement

class Body (HTMLelement):
    """
    Стандартный `HTML` элемент, тело.  
    """

    def __init__(self):
        """
        Создаёт стандартный `HTML` элемент, тело.  
        """

        super().__init__("body")

__version__ = "1.0.0"
__all__ = [
    "Body",
]