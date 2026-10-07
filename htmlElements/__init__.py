"""

"""

import os
import pyHTML
htmlElements_dir = os.path.dirname(os.path.abspath(__file__))

def init(head:pyHTML.HTMLelement) -> None:
    pyHTML.addFileText(head, f"{htmlElements_dir}/global.css", "style")
    pyHTML.addFileText(head, f"{htmlElements_dir}/image.css", "style")

from .text import text

__version__ = "0.0.0"
__all__ = [
    "init",
    "htmlElements_dir",
    "text",
    ]
