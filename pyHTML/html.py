"""

"""

from .htmlElement import HTMLelement
from .head import Head
from .body import Body

class HTML (HTMLelement):
    """
    Главный `"HTML"` элемент через который создается вся `HTML` страница.\
    Через этот класс можно создать целое дерево `"HTML"` элементов.
    """
    
    def __init__(self):
        """
        Создает и настрайвает класс, и затем возвращяет его.
        """

        super().__init__("html")
        
        self.doctype:str = "html"
        """"""
        self.lang:str = "en"
        """"""

        self.head:Head
        """"""
        self.body:Body
        """"""

    def getFullHTMLelement(self) -> str:
        """
        Создает и возвращяет полный `"HTML"` элемент. В нем будут атрибуты, и всё дерево `"HTML"` элементов что были добавленны, и в том порядке в котором они идут.
        """
        
        fullHTML = ""

        # Вставка "DOCTYPE".
        if self.doctype:
            fullHTML += "<!DOCTYPE " + self.doctype + ">"

        # Вставка "HTML".
        fullHTML += "<" + self.htmlElement

        ## Атрибуты.
        if self.attributes:
                fullHTML += " " + self.attributes

        ## Зарание подготовленные атрибуты.
        ### lang
        if self.lang:
            fullHTML += ' lang="' + self.lang + '"'
            
        fullHTML += ">"

        newChildren = []
        newChildren.append(self.head)
        newChildren.append(self.body)
        arrayParentElements = [newChildren]
        childCountStart = [0]
        childCountEnd = [len(newChildren) - 1]
        elementPosition = 0

        #def deleteElementFromArray() -> bool:
        #    """
        #    ВНУТРЕНЯЯ ФУНКЦИЯ.

        #    Удаляет элемент из массива.

        #    return <bool> -- Нужноли продолжать цыкл?
        #    * `True` - Да.
        #    * `False` - Нет.
        #    """
        #    nonlocal fullHTML, elementPosition, childCountEnd, childCountStart

        #    childCountEnd_number = childCountEnd[elementPosition]
        #    childCountStart_number = childCountStart[elementPosition]

        #    # Удаляеи массив из памяти.
        #    while childCountEnd_number >= childCountStart_number:
        #        print("₽₽₽", childCountEnd_number, childCountStart_number, elementPosition)
        #        del arrayParentElements[elementPosition]
        #        del childCountEnd[elementPosition]
        #        del childCountStart[elementPosition]
        #        elementPosition -= 1

        #        childCountEnd_number = childCountEnd[elementPosition]
        #        childCountStart_number = childCountStart[elementPosition]

        #    # Закрывает весь "HTML" тег.
        #    if elementPosition > -1:
        #        temp_childCountStart_number = childCountStart[elementPosition]
        #        temp_htmlClass = arrayParentElements[elementPosition]
        #        temp_htmlClass_element = temp_htmlClass[temp_childCountStart_number]

        #        fullHTML += temp_htmlClass_element.getCloseHead()
        #        childCountStart[elementPosition] += 1
        #    else:
        #        return True

        #    return False


        # Разворачивает дерево что были сохранены в "childrens".
        while elementPosition > -1:
            #time.sleep(0.1)
            #print("------------------")
            
            #print(1.1, elementPosition)
            #print(1.2, childCountStart)
            #print(1.3, childCountEnd)
            #print(1.4, arrayParentElements)

            childCountStart_number = childCountStart[elementPosition]
            childCountEnd_number = childCountEnd[elementPosition]

            htmlClass = arrayParentElements[elementPosition]
            htmlClass_element = htmlClass[childCountStart_number]

            #print(2.1, elementPosition)
            #print(2.2, childCountStart)
            #print(2.3, childCountEnd)
            #print(2.4, arrayParentElements)

            # Открывает "HTML" тег.
            isHTMLelement = True
            htmlClass_len = -1
            if isinstance(htmlClass_element, HTMLelement):
                fullHTML += htmlClass_element.getHead()
                htmlClass_len = len(htmlClass_element.childrens) - 1
            else:
                isHTMLelement = False

            # Запоминает массив с другими элементами.
            #print(htmlClass_element)
            if isHTMLelement:
                #print("len", htmlClass_len)
                if htmlClass_len > -1:
                    arrayParentElements.append(htmlClass_element.childrens)
                    childCountStart.append(0)
                    childCountEnd.append(htmlClass_len)
                    elementPosition += 1
                else:
                    fullHTML += htmlClass_element.getCloseHead()
                    childCountStart[elementPosition] += 1
            else:
                fullHTML += str(htmlClass_element)
                childCountStart[elementPosition] += 1

            childCountEnd_number = childCountEnd[elementPosition]
            childCountStart_number = childCountStart[elementPosition]

            #print(3.1, elementPosition)
            #print(3.2, childCountStart)
            #print(3.3, childCountEnd)
            #print(3.4, arrayParentElements)
            # Удаляеи массив из памяти.
            while childCountEnd_number < childCountStart_number:
                #print("₽₽₽", childCountEnd_number, childCountStart_number, elementPosition)

                try:
                    del arrayParentElements[elementPosition]
                    del childCountEnd[elementPosition]
                    del childCountStart[elementPosition]
                    elementPosition -= 1
                    childCountStart[elementPosition] += 1

                    childCountEnd_number = childCountEnd[elementPosition]
                    childCountStart_number = childCountStart[elementPosition]

                    temp_childCountStart_number = childCountStart[elementPosition]
                    temp_htmlClass = arrayParentElements[elementPosition]
                    temp_htmlClass_element = temp_htmlClass[temp_childCountStart_number -1]

                    fullHTML += temp_htmlClass_element.getCloseHead()
                except IndexError:
                    #print("ppp", childCountEnd_number, childCountStart_number, elementPosition)
                    break

            # Закрывает весь "HTML" тег.
            #if elementPosition > -1:
            #    temp_childCountStart_number = childCountStart[elementPosition]
            #    temp_htmlClass = arrayParentElements[elementPosition]
            #    temp_htmlClass_element = temp_htmlClass[temp_childCountStart_number]

            #    fullHTML += temp_htmlClass_element.getCloseHead()
            #    childCountStart[elementPosition] += 1

        #fullHTML += pyHTML.createHTMLfromAttributes(self.head, self.body, self.childrens)
        fullHTML += "</" + self.htmlElement + ">"
        return fullHTML
