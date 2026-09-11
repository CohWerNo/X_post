from typing import Self

class HTMLelement:
    """
    Создает и управляет `"HTML"` элементом, позволяет сохронять такиеже элементы, и создовать итоговый `"HTML"`.
    """

    def __init__(self, htmlElement:str=""):
        """
        Настрайвает и возвращяет класс.

        `<str> htmlElement` -- Это `"HTML"` элемент.
        """

        self.htmlElement:str = htmlElement

        self.attributes:str = ""

        self.childrens:list[Self | any] = []

    def append(self, *htmlElements:Self | any) -> None:
        """
        Добавляет несколько объектов в самый конец массива.

        `<HTMLelement | any> htmlElements` -- Добовляет несколько такиже классов, также есть возможность добавлять и другие классы, но все они будут преобразыванны в строку через `"str()"`.
        """
        for i in htmlElements:
            self.childrens.append(i)
            
    def prepend(self, *htmlElements:Self | any) -> None:
        """
        Добавляет несколько объектов в самое начало массива.

        `<HTMLelement | any> htmlElements` -- Добовляет несколько такиже классов, также есть возможность добавлять и другие классы, но все они будут преобразыванны в строку через `"str()"`.
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

    def getHead(self):
        """
        return <str> -- Возвращяет строку в виде неполного `"HTML"` элемента. Как пример `<html{ attributes}>`
        """

        head = "<" + self.htmlElement

        if self.attributes:
            head += " " + self.attributes

        head += ">"
        return head

    def getCloseHead(self):
        """
        return <str> -- Возвращяет строку в виде закрывающего `"HTML"` элемента. Как пример `</html>`
        """

        return "</" + self.htmlElement + ">"

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
