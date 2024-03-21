import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.dizionario = d.Dictionary()
        self.richWords = []

    def printDic(self, language):
        pass

    def searchWord(self, word, language):
        if len(self.dizionario._dict) == 0:
            self.dizionario.loadDictionary(f"resources/{language}.txt")
        richWord = rw.RichWord(word)
        self.richWords.append(richWord)
        if word in self.dizionario._dict:
            richWord.corretta = True
        else:
            richWord.corretta = False
        return self.richWords

    def searchWordLinear(self, word, language):
        if len(self.dizionario._dict) == 0:
            self.dizionario.loadDictionary(f"resources/{language}.txt")
        richWord = rw.RichWord(word)
        self.richWords.append(richWord)
        for parola in self.dizionario._dict:
            if parola == word:
                richWord.corretta = True
                break
            else:
                richWord.corretta = False
        return self.richWords

    def searchWordDichotomic(self, word, language):
        if len(self.dizionario._dict) == 0:
            self.dizionario.loadDictionary(f"resources/{language}.txt")
        richWord = rw.RichWord(word)
        self.richWords.append(richWord)
        inizio = 0
        fine = len(self.dizionario._dict)-1
        while inizio <= fine:
            richWord.corretta = False
            centro = (inizio+fine) // 2
            elemento_centrale = self.dizionario._dict[centro]
            if elemento_centrale == word:
                richWord.corretta = True
                break
            elif elemento_centrale > word:
                fine = centro - 1
            else:
                inizio = centro + 1
        return self.richWords
