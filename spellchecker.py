import time
import multiDictionary as md


class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        multiD = md.MultiDictionary()
        frase = txtIn.split(" ")
        lista = []
        i = 0
        time1 = time.time()
        for parola in frase:
            parola = replaceChars(parola)
            lista = multiD.searchWordDichotomic(parola, language)
        time2 = time.time()
        for element in lista:
            if element.corretta:
                pass
            else:
                print(element)
                i += 1
        print(f"{i} errori!")
        print(f"Tempo di esecuzione: {time2 - time1}")
        print("------------------------------")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n" +
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\/`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
        text = text.lower()
    return text
