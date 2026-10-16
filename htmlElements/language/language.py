"""
Небольшой модуль для управления несколикими языками в одном "py" файле. 
Этот модуль необходим для создания нескольких независемых "HTML" сайтов на разном языке. 

По этому модулю стойт знать главное!  
* Этот модуль не создан для создания нескольких языков в предела одного сайта.  
* Модуль покачто не поддерживает генераций нескольких "HTML" сайтов на разных языках, в пределах основного и единого "py" файла.  

Главная задача этого модуля в созданий нескольких "HTML" сайтов на разных языках, без копирования одного и тогоже кода. Но не в одном основном файле, а при активиций основного файла несколько раз с разными языками в итоге.  
"""

from typing import Any

import pyHTML

import os
language_dir = os.path.dirname(os.path.abspath(__file__))
"""Полный путь до папки "`language`", что находится в "htmlElements".  """

def init(head:pyHTML.HTMLelement):
    """
    Устанавливает `CSS` стили в `Head` `HTML` страницы.
    """
    #pyHTML.addFileText(head, f"{language_dir}/text.css", "style")


class Language:
    """
    Класс являеться структурой, в которой есть удобные подсказки и небольшое управление структурой через функций.  
    """

    def __init__(self):
        """
        Создаёт новый язык.
        """
        self.texts = {}
        """Эта переменная являеться главной в этом классе.  
        Именно в ней храняться все ключи вместе с их `HTML` текстом.
        """

    #def addLanguageText(self, textCode:str, text:str) -> None:
    #    index = 0
    #    while True:
    #        i = self.texts.get(textCode)
    #        if index:
    #            i += index

    #        if not i:
    #            self.texts[textCode] = text

    #        index += 1

    def setText(self, textKey:str, *htmlElements:pyHTML.HTMLelement|Any) -> list[pyHTML.HTMLelement|Any]:
        """
        Устанавливает ключ для `HTML` элементов.  

        Стандартные особенности:  
        * Если ключ не будет найден, то он создаться с переданными `HTML` элементами.  
        * Если ключ существует, то он будет перезаписан новыми переданными `HTML` элементами.  

        `<str> textKey` -- Текстовый ключь для переданных `HTML` элементов.  
        `<HTMLelement | Any> * htmlElements` -- `HTML` элементы, что будут сохранены под текстовым ключом.  

        `return <list[HTMLelement | Any]>` -- Возвращяет список из переданных "HTML" элементов.  
        """
        arr = list(htmlElements)
        self.texts[textKey] = arr
        return arr

    def getText(self, textKey:str) -> list[pyHTML.HTMLelement] | None:
        """
        Возврящяет список из указанного текстового ключа, в котороб будут находиться `HTML` элементы. Если такого ключа не существует, то возвращяеться "None".  

        `<str> textKey` -- Текстовый ключь для возвращения нужного текста.  

        `return <list[HTMLelement]>` -- Возвращяет список в котором находяться `HTML` элементы.  
        `return None` -- Если указанного ключа не существует, то вернёться "None".  
        """
        text = self.texts[textKey]
        if text:
            return text

        return None

class LanguageManagment:
    """
    Небольшой менеджер разных языков.  
    Он нужен для быстрого и удобного прямо из коробки создания нескольких `HTML` страниц со свойм языком.  
    """
    def __init__(self):
        """
        Создает менеджер языков, для управления и создания `HTML` страниц с разными языками.  
        """
        self.mainHTMLlanguage = ""
        """Основной язык что используеться на сайте.  
        Эта переменная нужна побольшей части для функций "`self.getLanguage()`".  
        """

        self.languages = {}
        """Словарь языков, в котором ключь это имя языка.  
        Значением являеться класс "`Language`".  
        """

    def setLanguage(self, htmlLanguage:str) -> Language:
        """
        Устанавливает новый язык.  

        Стандартные особенности:  
        * Если языка не будет существовать в переменной "`self.language`", то создасться новый язык под указанным ключом.  
        * Если язык будет существовать в переменной "`self.language`", то он перезапишеться на новое переданное значение.  

        `<str> htmlLanguage` -- Ключь под которым запомниться язык.  

        `return <Language>` -- Возвращяет класс "`Language`".  
        """
        lang = Language()
        self.languages[htmlLanguage] = lang
        return lang

    def getLanguageSelectively(self, htmlLanguage:str) -> Language | None:
        """
        Возвращяет нужный языковой класс "`Language`".  
        
        `<str> htmlLanguage` -- Ключь через который возвращяеться нужный язык.  

        `return <Language> -- Возвращяет язык.  
        `return None` -- Если ключа не существует, то возвращяеться "None".
        """
        lang = self.languages.get(htmlLanguage)
        if lang:
            return lang

        return None

    def getLanguage(self) -> Language | None:
        """
        Функция самостоятельно возвращяет основной язык.  
        Если небыла изменена переменная "`self.mainHTMLlanguage`" то по умолчанию вернёться "en" язык, если он существует.  

        Сама по себе функция активирует "`self.getLanguageSelectively()`" передавая переменную "`self.mainHTMLlanguage`".  
        
        `<str> htmlLanguage` -- Ключь через который возвращяеться нужный язык.  

        `return <Language> -- Возвращяет язык.  
        `return None` -- Если ключа не существует, то возвращяеться "None".  
        """
        return self.getLanguageSelectively(self.mainHTMLlanguage)

__versin__ = "0.0.0"
__all__ = [
    "init",

    "Language",
]
