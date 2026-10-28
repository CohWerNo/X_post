"""
"""

from typing import Any

class DefaultMessageError (Exception):
    """
    """

    def __init__(self, typeMessage:str, element:str, message:list[str]):
        """
        """

        self.typeMessage = typeMessage
        """"""
        self.element = element
        """"""
        self.message = message
        """"""

        super().__init__(self.__str__())

    def __str__(self) -> str:
        """`return <str>` -- Стандартное сообщение об ошибке.  """

        return f"{self.typeMessage}{self.element}{*self.message}"


def convertDictInString(dictVar:dict[Any, Any], typeElements:str) -> list[str]:
    """
    """
    finallyStringChar = []

    dictElements:dict[Any, Any]
    if typeElements == "keys":
        dictElements = dictVar.keys()

    elif typeElements == "values":
        dictElements = dictVar.values()

    else:
        raise TypeError(f"Типа \"{typeElements}\" не существует.\nСуществуют только эти типы: [ keys, values ].")

    for i in dictVar:
        finallyStringChar.append(i)

    return finallyStringChar

__version__ = "1.0.0"
__all__ = [
    "DefaultMessageError",

    "convertDictInString",
]
