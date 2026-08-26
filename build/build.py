import os
import subprocess

fullDirPath = os.path.dirname(os.path.abspath(__file__))
userPath = os.getcwd()

result = subprocess.run(f"python \"{fullDirPath}/include.py\"", capture_output=True, text=True)
if result.returncode == 0:
    print("Good Create one html: ", result.stdout)
else:
    print("Bad Create one html: ", result.stderr)
    exit()


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

arguments += " --use-short-doctype"

arguments += f" --input \"{userPath}/post.onehtml\""
arguments += f" --output \"{userPath}/bin/post.html\""


result = subprocess.run(arguments, shell=True, cwd=f"{fullDirPath}/html-minifier-next", capture_output=True, text=True, encoding="cp866")
if result.returncode == 0:
    print("Good Split size: ", result.stdout)
else:
    print("Bad Split size: ", result.stderr)
    exit()

if os.path.exists(f"{userPath}/post.onehtml"): os.remove(f"{userPath}/post.onehtml")