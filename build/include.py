from bs4 import BeautifulSoup
import os

fullDirPath = os.path.dirname(os.path.abspath(__file__))
userPath = os.getcwd()

#def removeCountDir(dir:str, file:str, count:int=1) -> str:
#    dirLen = len(dir)
#    i = dirLen
#    for letter in dir:
#        if letter == "/" or letter == "\\":
#            count -= 1
#        i -= 1
#        if count > 0:
#            return dir.split()

def splitDir(dir:str) -> list[str]:
    dir += "/"
    
    dirList = []
    text = ""
    for letter in dir:
        if letter == "/" or letter == "\\":
            if os.name == "posix":
                text += "/"
            else:
                text += "\\"
            dirList.append(text)
            text = ""
        else:
            text += letter
    return dirList


def inline_html(input_file, output_file):
    ##input_file = removeCountDir(fullDirPath, input_file)
    #splitDirection = splitDir(fullDirPath)
    #output_file = "".join(splitDirection) + output_file
    #splitDirection.pop(len(splitDirection) - 1)
    #splitDirection.append(input_file)
    #input_file = "".join(splitDirection)


    with open(input_file, 'r', encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    base_dir = os.path.dirname(os.path.abspath(input_file))
    
    # Заменяем <link rel="stylesheet" href="..."> на тег <style>
    for link in soup.find_all("link", rel=True):
        if 'stylesheet' in link.get("rel", []):
            href = link.get("href")
            if href and not href.startswith(("http://", "https://", "//")):
                css_path = os.path.join(base_dir, href)
                if os.path.exists(css_path):
                    with open(css_path, "r", encoding="utf-8") as css_file:
                        style_tag = soup.new_tag("style")
                        style_tag.string = css_file.read()
                        link.replace_with(style_tag)

                        
    # Заменяем <script src="..."> на тег <script> с кодом
    for script in soup.find_all("script", src=True):
        src = script.get("src")
        if src and not src.startswith(("http://", "https://", "//")):
            js_path = os.path.join(base_dir, src)
            if os.path.exists(js_path):
                with open(js_path, 'r', encoding="utf-8") as js_file:
                    new_script = soup.new_tag("script")
                    new_script.string = js_file.read()
                    # Копируем атрибуты (кроме src) если нужно, например type
                    for k, v in script.attrs.items():
                        if k != "src":
                            new_script[k] = v
                    script.replace_with(new_script)
                    
    with open(output_file, 'w', encoding="utf-8") as f:
        f.write(str(soup))

if __name__ == "__main__":
    inline_html(f"{userPath}/post.html", f"{userPath}/post.onehtml")
