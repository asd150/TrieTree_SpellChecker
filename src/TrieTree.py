import pickle
import os


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class TrieTree:
    def __init__(self):
        # List of all words from dictionary
        self.root = TrieNode()
        self.data = self.readFile()

    def readFile(self):
        wordList = []
        for line in open("words_alpha.txt"):
            currentWord = line.rstrip('\n')
            self.insert(currentWord)






    def insert(self,word):

        node = self.root
        for char in word:
            if not node.children.get(char):
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endOfWord = True

    def search(self,search_word):
        found = False
        CurrNode = self.root
        for char in search_word:
            if not CurrNode.children.get(char):
                return False
            elif CurrNode.endOfWord and found == False:
                return False
            else:
                CurrNode = CurrNode.children[char]
                found = CurrNode.endOfWord
        return found





exists =os.path.split(os.path.realpath(__file__))[0]+"\\words_alpha.txt"


print(os.path.exists(exists))


#
# initT = TrieTree()
# print(initT.search("animakl"))


if __name__ == '__main__':
    exists = os.path.split(os.path.realpath(__file__))[0] + "\\serialized.txt"
    initT = TrieTree()
    file = open('serialized.txt', 'wb')
    pickle.dump(initT, file, 0)
    file.close()

    file = open('serialized.txt','rb')
    TrieSer = pickle.load(file)
    file.close()
    print("animal === ",TrieSer.search("hhhhhhhhhhhhhhhhhhjjjjjjjjjjjjjjjjjjjjjjjjkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"))



    # if not exists:
    #     initT = TrieTree()
    #     file = open2





