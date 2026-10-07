import pyHTML

import htmlElements

def build():
    htmlPost = pyHTML.HTML()

    head = pyHTML.Head()
    body = pyHTML.Body()
    htmlPost.head = head
    htmlPost.body = body

    htmlElements.init(head)
    htmlElements.text.init(head)

    text1 = htmlElements.text.Text()
    textMonospace1 = htmlElements.text.TextMonospace()
    textMonospace1.append("it's monospace!")
    text1.append("Hi ", textMonospace1, " WoW.", " (FFF) ")

    body.append(text1)

    print(htmlPost.getFullHTMLelement())



def addCSSfile(htmlElement:pyHTML.HTMLelement, file:str) -> None:
    link = pyHTML.HTMLelement("style")

    with open(file, "r", encoding="utf-8") as f:
        link.childrens.append(f.read())

    htmlElement.childrens.append(link)
