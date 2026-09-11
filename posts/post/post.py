import pyHTML
from htmlElements.text import text

def build():
    htmlPost = pyHTML.HTML()

    head = pyHTML.Head()
    body = pyHTML.Body()

    htmlPost.head = head
    htmlPost.body = body

    text1 = text.Text()
    textMonospace1 = text.TextMonospace()
    textMonospace1.append("it's monospace!")
    text1.append("Hi ", textMonospace1, " WoW.")

    body.append(text1)

    print(htmlPost.getFullHTMLelement())