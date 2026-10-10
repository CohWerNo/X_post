"""
Самый обычный `HTML` элемент.  
Если нужно будет создать существующий `HTML` элемент которого нет по стандарту, или создать уникальный, то просто можно унаследовать этот класс.  
"""

from typing import Self

class HTMLelement:
    """
    Создает и управляет `HTML` элементом, позволяет сохронять такиеже элементы.  
    """

    def __init__(self, htmlElement:str=""):
        """
        Настрайвает и возвращяет класс.  

        `<str> htmlElement` -- Это `HTML` элемент.  
        """

        self.htmlElement:str = htmlElement
        """Сам `HTML` элемент.  """

        self.attributes:dict[str, any] = {}
        """Все различные атрибуты или переменные что будут записанны в `HTML` тег.  """

        self.childrens:list[Self | any] = []
        """Дети которые будут находится в нутри этого `HTML` элемента.  """

    def append(self, *htmlElements:Self | any) -> None:
        """
        Добавляет несколько объектов в самый конец массива.  

        `<HTMLelement | any> htmlElements` -- Добовляет несколько такиже классов, также есть возможность добавлять и другие классы, но все они будут преобразыванны в строку через "`str()`".  
        """
        for i in htmlElements:
            self.childrens.append(i)
            
    def prepend(self, *htmlElements:Self | any) -> None:
        """
        Добавляет несколько объектов в самое начало массива.  

        `<HTMLelement | any> htmlElements` -- Добовляет несколько такиже классов, также есть возможность добавлять и другие классы, но все они будут преобразыванны в строку через "`str()`".  
        """
        for i in htmlElements:
            self.childrens.insert(0, i)

    def insert(self, index:int, lockIndex=False, *htmlElements:Self | any) -> None:
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

    def getHead(self) -> str:
        """
        `return <str>` -- Возвращяет строку в виде неполного `HTML` элемента. Как пример `<html {attributes}>`.  
        """

        head = "<" + self.htmlElement

        attributes = self.getFullStringAttributes()
        if attributes:
            head += " " + attributes

        head += ">"
        return head

    def getCloseHead(self) -> str:
        """
        `return <str>` -- Возвращяет строку в виде закрывающего `HTML` элемента. Как пример `</html>`.  
        """

        return "</" + self.htmlElement + ">"

    def getFullStringAttributes(self) -> str:
        """
        Возвращяет полную строку аттрибутов, которые были заданны в переменной "`self.attributes`".  
        
        `return <str>` -- Возвращяет полную строку атрибутов что били указанны у элемента.  
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