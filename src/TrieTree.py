class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class TrieTree:
    def __init__(self):
        # List of all words from dictionary
        self.data = self.readFile()
    def readFile(self):

