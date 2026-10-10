import os
import sys
import subprocess

fullBuildPath = os.path.dirname(os.path.abspath(__file__))
"""Полный путь до папке где собирается проект.  """
fullRootPath = os.path.join(fullBuildPath, "../..")
"""Полный путь до корневой папки проекта.  """

# Добавляем корневую папку проекта.
sys.path.append(fullRootPath)



# Собираем файл в `HTML` страницу.
import pyHTML

import htmlElements

OUTPUT_FILE_NAME = f"{os.path.basename(fullBuildPath)}"
"""Имя конечного `HTML` файла.  """

BR = "<br>"
"""Удобно видеть в тексте "`{BR}`", вместо стандартного "`<br>`"."""

IDS = "<!--keepSpaces-->"
"""
IGNORE_DELETE_SPACE  
Специальный текст для "`html-minifier-next`" который не позволяет убирать пробелы в заданном блоке.  
"""

htmlPost = pyHTML.HTML(True, True)
"""Основная `HTML` страница.  """

htmlElements.init(htmlPost.head)
htmlElements.text.init(htmlPost.head)

text1 = htmlElements.text.Text()

text_monospace1 = htmlElements.text.TextMonospace()
text_monospace1.append("`Python`")
text_monospace2 = htmlElements.text.TextMonospace()
text_monospace2.append("`HTML`")

htmlMinifierNext_link = pyHTML.HTMLelement("a")
htmlMinifierNext_link.append("html-minifier-next")
htmlMinifierNext_link.attributes = {"href": "https://github.com/j9t/html-minifier-next"}

text1.append(
    f"Привет!{BR}{BR}",
    
    "Это небольшая ", text_monospace1, " проект, которая позволяет собирать вот такие ", text_monospace2, f" сайты.{BR}"
    "Этот проект позволяет легко создать небольшой и легкий по размерам локальный ", text_monospace2, f" сайт.{BR}{BR}"
    
    "Я ", htmlElements.addFastTag("b", "ОЧЕНЬ"), " благодарен сообществу что делают \"", htmlElements.addFastTag(text_monospace1.htmlElement, htmlMinifierNext_link), f"\"!{BR}",
    "Благодаря именно этим людям я сделал то что хотел.")

htmlPost.body.append(IDS, text1, IDS)

# Записываем итоговый `HTML` сайт в файл.
# Записываем этот файл обязательно в "`post.onehtml`", чтобы программа `html-minifier-next` увидело файл и начала его сокращять.
with open(f"{fullBuildPath}/post.onehtml", "w", encoding="utf=8") as f:
    f.write(htmlPost.getFullHTMLelement())



# Сокращяет размер `HTML` страницы.
## Заполняем программу основными флагами, для нужного сокращения `HTML` страницы.
arguments = "npx html-minifier-next"

arguments += " --no-continue-on-minify-error"

arguments += " --decode-entities"

arguments += " --merge-scripts"
arguments += " --minify-css true"
arguments += " --minify-js true"

arguments += " --collapse-attribute-whitespace"
arguments += " --collapse-boolean-attributes"
arguments += " --collapse-inline-tag-whitespace"
arguments += " --collapse-whitespace"

arguments += " --remove-attribute-quotes"
arguments += " --remove-comments"
arguments += " --remove-default-type-attributes"
arguments += " --remove-empty-attributes"
arguments += " --remove-empty-elements"
arguments += " --remove-redundant-attributes"
arguments += " --remove-tag-whitespace"

arguments += " --sort-attributes"
arguments += " --sort-class-names"

arguments += " --ignore-custom-fragments"
arguments += " \"(?<=<!--keepSpaces-->)[\\s\\S]*?(?=<!--keepSpaces-->)\""

arguments += f" --input \"{fullBuildPath}/post.onehtml\""
arguments += f" --output \"{fullBuildPath}/bin/{OUTPUT_FILE_NAME}.html\""


## Запускаем программу которая сократит размер всей `HTML` странице.
result = subprocess.run(arguments, shell=True, cwd=f"{fullRootPath}/build/html-minifier-next", capture_output=True, text=True, encoding="utf-8")
if result.returncode == 0:
    print("Good Split size: ", result.stdout)
else:
    print("Bad Split size: ", result.stderr)
    print("main", 2)
    exit(2)

if os.path.exists(f"{fullBuildPath}/post.onehtml"): os.remove(f"{fullBuildPath}/post.onehtml")

exit(0)