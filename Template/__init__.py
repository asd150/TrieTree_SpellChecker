# class TrieNode:
#     def __init__(self):
#         self.children  = {}
#         self.end = False
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#         self.keys = ["arth","desai","ab"]
#         self.wordList = []
#
#     def buildTree(self):
#         for word in self.keys:
#             self.insertKey(word)
#
#     def insertKey(self,word):
#         node = self.root
#         for char in list(word):
#             if not node.children.get(char):
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.end = True
#     def recursion(self,node,prefix):
#         if node.end:
#             self.wordList.append(prefix)
#
#         for key,val in node.children.items():
#             self.recursion(node.children[key],prefix+key)
#
#
#     def autoSuggestion(self,key):
#         node = self.root
#         temp = ""
#         for i in key:
#             if not node.children.get(i):
#                 return False
#             node = node.children[i]
#             temp = temp+i
#         self.recursion(node,temp)
#
#
#
# k = Trie()
# k.buildTree()
# print(k.root.children)
# print(k.autoSuggestion("ra"))
# print(k.wordList)
# k.insertKey("rabbit")
#
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.wordList = []


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            if not node.children.get(char):
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        found = False
        for char in word:
            if not node.children.get(char):
                return False
            elif node.end and found == False:
                return False
            else:
                node = node.children[char]
                found = node.end
        return found

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        found = True
        for char in prefix:
            if not node.children.get(char):
                return False
            else:
                node = node.children[char]
        return found
    def recursion(self,node,prefix):
        if node.end:
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






obj = Trie()
obj.insert("arth")
obj.insert("asd")

obj.insert("aaa")

obj.insert("arath")


obj.insert("lion")
obj.insert("lions")
obj.insert("sss")



c=obj.search("arthyyy")

print(c)
# v = obj.startsWith("p")
obj.autoCompletion("ar")

print(obj.wordList)
# print(v)