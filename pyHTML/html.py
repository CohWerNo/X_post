"""
"`html.py`" являеться главным модулем для создания локальной `HTML` страницы.  
Именно в этом модуле есть возможность создать всю `HTML` страницы, так-как в самом `HTML` документе, самым главным тегом и самым первым всегда являеться `<html>`.  
"""

from .htmlElement import HTMLelement_Empty, HTMLelement
from .head import Head
from .body import Body

class HTML (HTMLelement):
    """
    Главный `"HTML"` элемент через который создается вся `HTML` страница.  
    Через этот класс можно создать целое дерево `"HTML"` элементов.  
    """
    
    def __init__(self):
        """
        Создаёт класс для удобной оаботы с `HTML` сайтом на `Python`.  
        """

        super().__init__("html")
        
        self.doctype:str = "html"
        """Тип документа который будет использоватся.  
        Если переменная будет пустой, то `HTML` элемент "`<DOCTYPE {self.doctype}>`" не будет установлен.  

        `default = "html"`.  
        """

        self.lang:str = "en"
        """Язык `HTML` страницы.  

        `default = "en"`  
        """

        self.title = ""
        """Загаловок страницы.  
        Если переменная будет пустой, то `HTML` элемент "`<title>{self.title}</title>`" не будет создан.  
        """

        self.charset = "UTF-8"
        """Кодировка символов на сайте.  
        Если переменная будет пустой, то `HTML` элемент "`<meta charset="{self.charset}">`" не будет создан.  

        `default = "UTF-8"`  
        """

        self.deviceScale = "width=device-width, initial-scale=1"
        """Указывает единый размер сайта для разных устройств.  
        Если переменная будет пустой, то `HTML` элемент не будет создан.  

        `default = "width=device-width, initial-scale=1"`  

        По умолчанию будет созданн вот такой `HTML` элемент, в элементе "`<html><head>`"  
        ```html
        <meta name="viewport" content="width=device-width, initial-scale=1">
        ```
        """

        self.head:Head
        """Голова `HTML` страницы.  """

        self.body:Body
        """Тело `HTML` страницы.  """

    def getFullHTMLelement(self) -> str:
        """
        Создает и возвращяет полный `HTML` элемент.  
        В `HTML` элементе будут все написанные атрибуты, и всё дерево `HTML` элементов что были добавленны.  
        Все `HTML` элементы будут расположенны в том порядке, в котором они идут.  
        """
        
        fullHTML = ""

        # Вставка "DOCTYPE".
        if self.doctype:
            fullHTML += "<!DOCTYPE " + self.doctype + ">"

        # Вставка "HTML".
        fullHTML += "<" + self.htmlElement

        ## Атрибуты.
        self.attributes["lang"] = self.lang
        fullHTML += " " + self.getFullStringAttributes()
            
        fullHTML += ">"

        # Заполняем `HTML` элемент "`head`".
        if self.head:
            if self.charset:
                meta = HTMLelement_Empty("meta")
                meta.attributes = {
                    "charset": self.charset,
                }
                self.head.append(meta)

            if self.deviceScale:
                meta = HTMLelement_Empty("meta")
                meta.attributes = {
                    "name": "viewport",
                    "content": "width=device-width, initial-scale=1",
                }
                self.head.append(meta)

            if self.title:
                title = HTMLelement("title")
                title.append(self.title)
                self.head.append(title)

        # Заполнение `HTML` элементов в итоговый текст.
        # Собираются все дети что находяться у `HTML` элементов.
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
            isHTMLemptyElement = False
            htmlClass_len = -1
            if isinstance(htmlClass_element, HTMLelement):
                fullHTML += htmlClass_element.getHead()
                htmlClass_len = len(htmlClass_element.childrens) - 1

            elif isinstance(htmlClass_element, HTMLelement_Empty):
                fullHTML += htmlClass_element.getHead()
                isHTMLelement = False
                isHTMLemptyElement = True

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

            elif isHTMLemptyElement:
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
