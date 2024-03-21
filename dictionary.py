class Dictionary:
    def __init__(self):
        self._dict = []

    def loadDictionary(self, path):
        f = open(path, 'r', encoding='UTF-8')
        line = f.readline()
        while len(line) > 0:
            self._dict.append(line.strip())
            line = f.readline()
        f.close()

    def printAll(self):
        for word in self._dict:
            print(word)

    @property
    def dict(self):
        return self._dict
