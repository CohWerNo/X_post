"""
Голова для запоминания нужной информаций, скрывая её от пользователя.  
"""

from .htmlElement import HTMLelement

class Head (HTMLelement):
    """
    Стандартный `HTML` элемент, голова.  
    """

    def __init__(self):
        """
        Создаёт стандартный `HTML` элемент, голова.  
        """

        super().__init__("head")

__version__ = "1.0.0"
__all__ = [
    "Head",
]