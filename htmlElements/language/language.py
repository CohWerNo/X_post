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
        `<HTMLelement | Any> *htmlElements` -- `HTML` элементы, что будут сохранены под текстовым ключом.  

        `return <list[HTMLelement | Any]>` -- Возвращяет список из переданных "HTML" элементов.  
        """
        arr = list(htmlElements)
        self.texts[textKey] = arr
        return arr

    def getText(self, textKey:str) -> list[pyHTML.HTMLelement]:
        """
        Возврящяет список из указанного текстового ключа, в котороб будут находиться `HTML` элементы. Если такого ключа не существует, то возвращяеться "None".  

        `<str> textKey` -- Текстовый ключь для возвращения нужного текста.  

        `return <list[HTMLelement]>` -- Возвращяет список в котором находяться `HTML` элементы.  
        `return None` -- Если указанного ключа не существует, то вернёться "None".  
        """
        text = self.texts.get(textKey)
        if text:
            return text

        raise LanguageTextKeyNotFoundError(textKey, "Не существует в этом языке.", "Чтобы это исправить добавте этот ключь или исправте его название.", allTextKey=self.texts)

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

    def getLanguageSelectively(self, htmlLanguage:str) -> Language:
        """
        Возвращяет нужный языковой класс "`Language`".  
        
        `<str> htmlLanguage` -- Ключь через который возвращяеться нужный язык.  

        `return <Language> -- Возвращяет язык.  
        `return None` -- Если ключа не существует, то возвращяеться "None".
        """
        lang = self.languages.get(htmlLanguage)
        if lang:
            return lang

        raise LanguageNotFoundError(htmlLanguage, "Небыл найден в базе с языками.", "Чтобы исправить ошибку добавте этот язык в базу, или исправте название на существующие.",  allLanguage=self.languages)

    def getLanguage(self) -> Language:
        """
        Функция самостоятельно возвращяет основной язык.  
        Если небыла изменена переменная "`self.mainHTMLlanguage`" то по умолчанию вернёться "en" язык, если он существует.  

        Сама по себе функция активирует "`self.getLanguageSelectively()`" передавая переменную "`self.mainHTMLlanguage`".  
        
        `<str> htmlLanguage` -- Ключь через который возвращяеться нужный язык.  

        `return <Language> -- Возвращяет язык.  
        `return None` -- Если ключа не существует, то возвращяеться "None".  
        """
        return self.getLanguageSelectively(self.mainHTMLlanguage)


class _DefaultMessage (Exception):
    """
    Класс создан для стандартных сообщений в этом модуле.  
    Его главная задача это сделать удобное однообразие сообщений, чтобы мгновенно считывать сообщения при разных ошибках.  
    """

    def __init__(self, *message:object):
        """
        Создаёт класс для стандартных сообщений в этом модуле.  
        """

        super().__init__(*message)

        self.message = message
        """Сообщение об ошибке.  """

    def __str__(self) -> str:
        """
        `return <str>` -- Возвращяет стандартное сообщение об ошибке.  
        """
        return "\n".join(self.message)

    def _convertDictInList(self, dictVar:dict[str, Any]) -> list[str]:
        """
        Конвентирует все ключи что были в переданном словаре в список с ключами.  

        Данная функция нужна только для ошибок в этом модуле, за её пределами использовать её не желательно. 

        `<dict[str, Any]> dictVar` -- Словарь из которого нужно достать все ключи.  

        `return <list[str]>` -- Возвращяет список со всеми найденными ключами из переданного славоря.  
        """

        allLanguageChars = ["[", " "]
        first = False
        for i in dictVar:
            if first:
                allLanguageChars.append(", ")
            else:
                first = True

            allLanguageChars.append(i)

        allLanguageChars.append(" ")
        allLanguageChars.append("]")

        return allLanguageChars

    def _convertDictInString(self, dictVar:dict[str, Any]) -> str:
        """
        Конвертирует все ключи что были в переданном словаре в строку. 

        Данная функция нужна только для ошибок в этом модуле, за её пределами использовать её не желательно. 

        Функция работает на основе функций "`self._convertDictInList`". 

        `<dict[str, Any]> dictVar` -- Словарь из которого нужно достать все ключи.

        `return <str>` -- Возвращяет строку в которой будут последовательно поставленные ключи, что были найдены в словаре.  
        """
        return "".join(self._convertDictInList(dictVar))

    def _getDefaultMessage(self, startMessage:str, objectString:str, message:str) -> str:
        """
        Возвращяет стандартный текст об ошибке.  
        Эта функция нужна для удобного однообразия.  

        Данная функция нужна только для ошибок в этом модуле, за её пределами использовать её не желательно. 

        `<str> startMessage` -- Начальное сообщение. Оно будет ставиться в самом начале всего сообщкния.  
        `<str> objectString` -- Специальное сообщение об объекте. Эта переменная нужна только для видимого обозначения объекта по которому и была ошибка.  
        `<str> message` -- Сообщение об ошибке.  

        `return <str>` -- Возвращяет однотипную строку об ошибке.  
        """
        return f"{startMessage} \"{objectString}\" -- {message}"

class LanguageTextKeyNotFoundError (_DefaultMessage):
    """
    Ошибка говорящяя о том что небыл найден ключь, где либо.  

    Данную ошибку стойт вызывать, когда в ожидаемом месте небыл найден ключь.  
    """

    def __init__(self, textKey:str, *message:str, allTextKey:dict[str, str] | None):
        """
        Создаёт класс со стандартными настройками, для вывада правильного сообщения об ошибке.  

        `<str> textKey` -- Текстовый ключь из-за которого и произошла ошибка.  
        `<str> *message` -- Сообщение об ошибке которое будет объединено в одно. Каждый новый текст будет разделяться новой строкой.  
        `<dict[str, str] | None> allTextKey` -- Словарь из которого нужно достать все ключи, что будут говорить о всех доступных ключах. 
        * `None` - Если переменна не будет передана, то список из существующих доступных ключей небудет создана.
        """

        super().__init__(textKey, message)

        self.message = message
        """Сообщение об ошибке.  """
        self.textKey = textKey
        """Текстовый ключь из-за которого и произошла эта ошибка.  """
        self.allTextKey = ""
        """Все ключи что будут найдены в переданном словаре.  
        Все ключи будут заранее записаны в строке.  """

        if allTextKey:
            self.allTextKey = self._convertDictInString(allTextKey)

    def __str__(self):
        """
        `return <str>` -- Возвращяет стандартное сообщение об ошибке.  
        """

        allTextKey = ""
        if self.allTextKey:
            allTextKey = f"\nВсе существующие ключи: \"{self.allTextKey}\""

        return self._getDefaultMessage("Ключь", self.textKey, "\n".join(self.message)) + allTextKey

class LanguageNotFoundError (_DefaultMessage):
    """
    Ошибка говоращяя о том что язык небыл найден где либо.  

    Данную ошибку стойт вызывать если язык небыл найден в ожидаемом месте.  
    """

    def __init__(self, language:str, *message:str, allLanguage:dict[str, str] | None):
        """
        Создаёт переменные для правильного сообщения об ошибке.  

        `<str> language` -- Язык который небыл найден.  
        `<str> *message` -- Сообщение об ошибке которое будет объединено в одно. Каждый новый текст будет разделяться новой строкой.  
        `<dict[str, str] | None> allLanguage` -- Словаря из языков. В качестве текста будут браться ключи.  
        * `None` - Если переменная не будет переданна, то список из существующих языков не будет создан.  
        """

        super().__init__(language, message)

        self.message = message
        """Сообщение об ошибке.  """
        self.language = language
        """Язык.  """
        self.allLanguage = ""
        """Все языки что были в переданном "`LanguageManagment`".  """

        # Заполняем переменную "`self.allLanguage`" всеми языками что есть в переданном "`LanguageManagment`".
        if allLanguage:
            self.allLanguage = self._convertDictInString(allLanguage)

    def __str__(self) -> str:
        """
        `return <str>` -- Возвращяет стандартное сообщение об ошибке.  
        """

        allLanguage = ""
        if self.allLanguage:
            allLanguage = f"\nСписк существующих языков: \"{self.allLanguage}\""

        return self._getDefaultMessage("Язык", self.language, "\n".join(self.message)) + allLanguage


__versin__ = "1.0.0"
__all__ = [
    "init",

    "Language",
    "LanguageManagment",

    "LanguageTextKeyNotFoundError",
    "LanguageNotFoundError",
]
