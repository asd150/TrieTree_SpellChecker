import pickle
import os
import copy
import numpy as np
import string
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

    def readParagraph(self,paragraph):
        all_incorrect_words = {}

        paragraph = paragraph.split(" ")
        for word in paragraph:
            candidateWords = []
            if len(word)>0:
                # print("-->",word)
                currLen = len(word)
                lists = self.check(word)


                # incorrect word
                newL = []
                if len(lists) > 0:
                    for i in range(len(lists)):

                        if len(lists[i]) < len(word)+5:
                            newL.append(lists[i])
                for i in range(len(newL)):
                    editDistance = self.edit_distance(word,newL[i])
                    candidateWords.append((newL[i],editDistance))
            candidateWords = sorted(candidateWords,key = lambda x : x[1])
            all_incorrect_words[word] = candidateWords[:5]

        return all_incorrect_words









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
            return []
        else:
            word_ = word
            while word_ != '':
                word_ = word_[:len(word_)-1]
                # print(word_)
                # print('self.autoCompletion(word_)',self.autoCompletion(word_))
                if self.autoCompletion(word_)==None:
                    # print(word_)
                    result = copy.deepcopy(self.wordList)
                    self.wordList.clear()

                    return result

    def diff(self,a, b):
        if a == b:
            return 0
        else:
            return 1

    def edit_distance(self,x, y):
        m = len(x)
        n = len(y)
        E = np.zeros((m + 1, n + 1))
        for i in range(m + 1):
            E[i][0] = i
        for j in range(n + 1):
            E[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                E[i][j] = min(1 + E[i - 1][j], 1 + E[i][j - 1], self.diff(x[i - 1], y[j - 1]) + E[i - 1][j - 1])

        return E[m][n]






exists =os.path.split(os.path.realpath(__file__))[0]+"\\words_alpha.txt"


print(os.path.exists(exists))


#
# initT = TrieTree()
# print(initT.search("animakl"))


if __name__ == '__main__':
    # Training Phase
    # exists = os.path.split(os.path.realpath(__file__))[0] + "\\serialized.txt"
    # initT = TrieTree()
    # file = open('serialized.txt', 'wb')
    # pickle.dump(initT, file, 0)
    # file.close()

    # Serialized Version
    # file = open('serialized.txt','rb')
    # TrieSer = pickle.load(file)
    # file.close()
    #
    s = "string. Witht. animmm?"
    s = s.translate(str.maketrans('', '', string.punctuation)).lower()

    T = TrieTree()
    incorrect = T.readParagraph(s)

    for key,val in incorrect.items():
        if len(val)>0:
            print(key,"--->", val)












