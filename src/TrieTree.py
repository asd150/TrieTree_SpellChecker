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
        words  =[]
        all_incorrect_words = {}

        paragraph = paragraph.split(" ")
        for word in paragraph:
            if word not in words:
                words.append(word)
                candidateWords = []
                if len(word)>0 and self.search(word) == False:
                    # print("-->",word)

                    lists = self.check(word)
                    candidateWords = sorted(lists, key=lambda x: x[1])
                    # recommended words for a given incorrenc

                    # incorrect word
                #     newL = []
                #     if len(lists) > 0:
                #         for i in range(len(lists)):
                #
                #             if len(lists[i]) < len(word)+5:
                #                 newL.append(lists[i])
                #     for i in range(len(newL)):
                #         editDistance = self.edit_distance(word,newL[i])
                #         if editDistance <=3:
                #             candidateWords.append((newL[i],editDistance))
                # candidateWords = sorted(candidateWords,key = lambda x : x[1])
                if all_incorrect_words.get(word) == None:
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
        result = []
        retRes = []
        if self.search(word):
            return []
        else:
            word_ = word
            while word_ != word[0]:
                word_ = word_[:len(word_)-1]
                if self.autoCompletion(word_)==None:
                    # print(word_)
                    # result = copy.deepcopy(self.wordList)
                    for i in self.wordList:

                        if len(i) < len(word)+4:

                            ed = self.edit_distance(word,i)
                            if ed < 3:
                                if i not in result:
                                    result.append(i)
                                    retRes.append((i,ed))


                    self.wordList.clear()

        return retRes

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


# exists =os.path.split(os.path.realpath(__file__))[0]+"\\words_alpha.txt"
#
#
# print(os.path.exists(exists))




if __name__ == '__main__':
    # Training Phase
    # exists = os.path.split(os.path.realpath(__file__))[0] + "\\serialized.txt"
    # initT = TrieTree()
    # initT.insert("trie")
    # initT.insert("bst")
    #
    # file = open('serialized.txt', 'wb')
    # pickle.dump(initT, file, 0)
    # file.close()

    # Serialized Version
    file = open('serialized.txt','rb')
    TrieSer = pickle.load(file)
    file.close()
    # # #
    # # s = "string. Witht. animmm?"
    s = "Trie is an efficient information retrievl data structure. Using trie, search complexities can be brought to optimal " \
        "limit (key length). If we store keys in binary search tree, a well balanced BST will need time proportonal " \
        "to M log N, where M is maximum string length and N is nuber of keys in tree. Using trie we can search the key in O(M) time. " \
        "Howerer, the penalty is on Trie storage requiremets"
    s = s.translate(str.maketrans(' ', ' ', string.punctuation)).lower()
    # # print(s)
    # #
    #
    # # incorrect = TrieSer.readParagraph(s)
    # #
    # #
    # # #
    #
    #
    # trie  =TrieTree()
    x = TrieSer.readParagraph(s)

    for key,val in x.items():
        if len(val)>0:
            print(key,"--->", val)








