import pyHTML

def createHTMLtree0(*attributes:list | tuple | pyHTML.HTMLelement | any) -> str:
    """"""

    if len(attributes) < 1:
        return ""

    def checkTypeAndSet(item:any):
        nonlocal htmlInner

        if isinstance(item, pyHTML.HTMLelement):
            htmlInner += item.getFullHTMLelement()
        else:
            htmlInner += str(item)
        
    htmlInner = ""

    for globalAttribute in attributes:
        if len(globalAttribute) < 1:
            continue

        if isinstance(globalAttribute, list) or isinstance(globalAttribute, tuple):
            for i in globalAttribute:
                checkTypeAndSet(i)
        else:
            checkTypeAndSet(globalAttribute)
        

    return htmlInner
