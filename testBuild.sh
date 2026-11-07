rootFolder=$(cd -- "$(dirname -- "$0")" && pwd)

export PYTHONPATH="$rootFolder:$PYTHONPATH"

folder_lib="$rootFolder/lib/"
folder_lib_htmlElements="$folder_lib/htmlElements/"
folder_htmlElements_language="$folder_lib_htmlElements/language/"

python "$folder_lib_htmlElements/error.py"
