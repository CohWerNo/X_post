"""
Самый обычный `HTML` элемент.  
Если нужно будет создать существующий `HTML` элемент которого нет по стандарту, или создать уникальный, то просто можно унаследовать этот класс.  
"""

from typing import Self, Any


class HTMLelement_Empty:
    """
    Класс позволяет создать пустой `HTML` элемент, если элемент не обязательно закрывать.  
    """

    def __init__(self, htmlElement:str=""):
        """
        Создаёт класс пустого `HTML` элемента.  
        """

        self.htmlElement:str = htmlElement
        """Сам `HTML` элемент.  """

        self.attributes:dict[str, Any] = {}
        """Все различные атрибуты или переменные что будут записанны в `HTML` тег.  """

    def getHead(self) -> str:
        """
        `return <str>` -- Возвращяет строку в виде пустого `HTML` элемента. Как пример `<html {attributes}>`.  
        Также вместе с головой, возвращяються и введённые атрибуты.  
        """

        head = "<" + self.htmlElement

        attributes = self.getFullStringAttributes()
        if attributes:
            head += " " + attributes

        head += ">"
        return head

    def getFullStringAttributes(self) -> str:
        """
        `return <str>` -- Возвращяет полную строку аттрибутов, которые были заданны в переменной "`self.attributes`".  
        
        """

        if not isinstance(self.attributes, dict) and len(self.attributes):
            return ""
        
        fullString = ""

        addSpace = False

        for key, value in self.attributes.items():
            if addSpace:
                fullString += " "
            else:
                addSpace = True
            fullString += f"{key}=\"{str(value)}\""

        return fullString

    def __str__(self) -> str:
        """
        `return <str>` -- Возвращяет переменную `self.htmlElement`.  
        """
        return self.htmlElement

    def __len__(self) -> int:
        """
        `return <int>` -- Возвращяет число, что означает количество символов у переменной `self.htmlElement`.  
        """
        return len(self.htmlElement)


class HTMLelement (HTMLelement_Empty):
    """
    Класс являеться самым обычным `HTML` элементом. 
    """

    def __init__(self, htmlElement:str=""):
        """
        Настрайвает и возвращяет класс.  

        `<str> htmlElement` -- Это `HTML` элемент.  
        """

        super().__init__(htmlElement)

        self.childrens:list[Self | Any] = []
        """Дети которые будут находится в нутри этого `HTML` элемента.  """

    def append(self, *htmlElements:Self | Any) -> None:
        """
        Добавляет несколько объектов в самый конец массива.  

        `<HTMLelement | any> htmlElements` -- Добовляет несколько такиже классов, также есть возможность добавлять и другие классы, но все они будут преобразыванны в строку через "`str()`".  
        """
        for i in htmlElements:
            self.childrens.append(i)
            
    def prepend(self, *htmlElements:Self | Any) -> None:
        """
        Добавляет несколько объектов в самое начало массива.  

        `<HTMLelement | any> htmlElements` -- Добовляет несколько такиже классов, также есть возможность добавлять и другие классы, но все они будут преобразыванны в строку через "`str()`".  
        """
        for i in htmlElements:
            self.childrens.insert(0, i)

    def insert(self, index:int, lockIndex=False, *htmlElements:Self | Any) -> None:
        """
        Добавляет несколько объектов в указанный индекс.  

        `<int> index` -- Индекс по которому будут добавленны объекты в массив.  
        `<bool> lockIndex = False` -- Указывает то как именно нужно добовлять объекты в массив.  
        `* False` - Добовляет объекты по указанному индексу, и никак его не меняет.  
        `* True` - Добовляет объекты, и к исходному индексу добовляет по `+1`, выстрайвая объекты в ряд.  
        `<HTMLelement | any> htmlElements` -- Добовляет несколько такиже классов, также есть возможность добавлять и другие классы, но все они будут преобразыванны в строку через `"str()"`.  
        """
        for i in htmlElements:
            self.childrens.insert(index, i)
            if not lockIndex:
                index += 1

    def getCloseHead(self) -> str:
        """
        `return <str>` -- Возвращяет строку в виде закрывающего `HTML` элемента. Как пример `</html>`.  
        """
        return "</" + self.htmlElement + ">"



__version__ = "1.0.1"
__all__ = [
    "HTMLelement_Empty",
    "HTMLelement",
]
