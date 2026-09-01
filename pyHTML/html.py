from .htmlElement import HTMLelement

from .head import Head
from .body import Body

class HTML (HTMLelement):
    """
    This Class
    """
    
    def __init__(self):
        """"""

        super().__init__("html")
        
        self.doctype:str = "html"
        self.lang:str = "en"

        self.head:Head
        self.body:Body

    def getFullHTMLelement(self) -> str:
        """"""
        
        fullHTML = ""

        # Вставка "DOCTYPE".
        if self.doctype:
            self.fullHTML += "<!DOCTYPE " + self.doctype + ">"

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
        fullHTML += self.createHTMLfromAttributes(self.head, self.body, self.childrens)
        fullHTML + "</" + self.htmlElement + ">"
        return self.fullHTML