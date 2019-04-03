import pickle
import os
import copy

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class TrieTree:
    def __init__(self):
        # List of all words from dictionary
        self.root = TrieNode()
        self.data = self.readFile()
        self.wordList = []



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

    def recursion(self,node,prefix):
        if node.endOfWord:
            self.wordList.append(prefix)


        for key,val in node.children.items():
            self.recursion(node.children[key],prefix+key)





    def autoCompletion(self,prefix):
        tempKey = ""
        node = self.root

        for char in prefix:
            if not node.children.get(char):
                return False

            node = node.children[char]
            tempKey = tempKey+char
        self.recursion(node,tempKey)

    def check(self, word):
        if self.search(word):
            return True
        else:
            word_ = word
            while word_ != '':
                word_ = word_[:len(word_)-1]
                print(word_)
                print('self.autoCompletion(word_)',self.autoCompletion(word_))
                if self.autoCompletion(word_)==None:
                    print(word_)
                    result = copy.deepcopy(self.wordList)
                    self.wordList.clear()

                    return result





exists =os.path.split(os.path.realpath(__file__))[0]+"\\words_alpha.txt"


print(os.path.exists(exists))


#
# initT = TrieTree()
# print(initT.search("animakl"))


if __name__ == '__main__':
    # exists = os.path.split(os.path.realpath(__file__))[0] + "\\serialized.txt"
    # initT = TrieTree()
    # file = open('serialized.txt', 'wb')
    # pickle.dump(initT, file, 0)
    # file.close()

    file = open('serialized.txt','rb')
    TrieSer = pickle.load(file)
    file.close()
    print("animal === ",TrieSer.check("animmmm"))
    # TrieSer.autoCompletion("hhhhhhhhhhhhhhhhhhjjjjjjjjjjjjjjjjjjjjjjj")




    # if not exists:
    #     initT = TrieTree()
    #     file = open2





