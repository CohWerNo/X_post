class HTMLelement:
    """"""

    def __init__(self, htmlElement:str=""):
        """"""

        self.htmlElement:str = htmlElement

        self.attributes:str = ""

        self.childrens:list[HTMLelement | any] = []

    def append(self, *htmlElements:HTMLelement) -> None:
        """"""
        for i in htmlElements:
            self.childrens.append(i)
            
    def prepend(self, *htmlElements:HTMLelement) -> None:
        """"""
        for i in htmlElements:
            self.childrens.insert(0, i)

    def insert(self, index:int, *htmlElements:HTMLelement) -> None:
        """"""
        for i in htmlElements:
            self.childrens.insert(index, i)
            index += 1

    def getFullHTMLelement(self) -> str:
        """"""

        fullHTMLelement = "<" + self.htmlElement

        # Атрибуты.
        if self.attributes:
            fullHTMLelement += " " + self.attributes

        fullHTMLelement += ">"
        fullHTMLelement += self.createHTMLfromChildrens()
        fullHTMLelement += "</" + self.htmlElement + ">"
        return fullHTMLelement

    def createHTMLfromAttributes(self, *attributes:list|tuple|HTMLelement|any) -> str:
        """"""
        if len(attributes) < 1:
            return ""

        def checkTypeAndSet(item:any):
            nonlocal htmlInner

            typeClass = item.__name__

            if typeClass != "HTMLelement":
                htmlInner += item.getFullHTMLelement()

            htmlInner += str(item)

        htmlInner = ""

        for globalAttribute in attributes:
            if len(globalAttribute) < 1:
                continue

            typeClass = globalAttribute.__name__

            if typeClass == "list" and typeClass == "tuple":
                for i in globalAttribute:
                    checkTypeAndSet(i)

            checkTypeAndSet(globalAttribute)
            

        return htmlInner
            
    def __str__(self) -> str:
        """"""
        return self.getFullHTMLelement()