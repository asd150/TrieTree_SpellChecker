
# from tkinter import *
import tkinter as tk



# # from tkinter import *
# # from math import *
# # def evaluate(event):
# #     res.configure(text = "Ergebnis: " + entry.get())
# # w = Tk()
# # Label(w, text="Your Expression:").pack()
# # entry.bind("<Return>", evaluate)
# #
# # entry.pack()
# # res = Label(w)
# # res.pack()
# # w.mainloop()
# # entry = Entry(w)
# # from tkinter import *
# #
# #
# # def show_entry_fields():
# #     print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
# #
# #
# # master = Tk()
# # Label(master, text="First Name").grid(row=0)
# # Label(master, text="Last Name").grid(row=1)
# #
# # e1 = Entry(master)
# # e2 = Entry(master)
# #
# # print(e1)
# #
# # e1.grid(row=0, column=1)
# # e2.grid(row=1, column=1)
# #
# # Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
# # Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
# #
# # mainloop()
# # ainloop( )

# def printingFunc():
#     string = str(testEntry.get())
#     print(string)
# window  = tk.Tk()
#
# window.geometry("400x400")
#
# testEntry = tk.Text()
# testEntry.grid(column = 0,row = 1)
# button1 = tk.Button(text = "click me",master= window,command = printingFunc)
# button1.grid(column = 1,row = 1)
# window.mainloop()
#
#



from tkinter import *
root=Tk()

textRec = ""
class TrieTree:
    def __init__(self):
        self.txt = "Creating Trie Tree"
        self.list = []
    def printF(self):
        print(self.txt)
def helper(str):
    str = str.split(" ")
    for i in str:
        trie.list.append(i)
    print(trie.list)


def retrieve_input():
    inputValue=str(textBox.get("1.0","end-1c"))
    helper(inputValue)




textBox=Text(root, height=2, width=10)

textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Commit",
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button

buttonPrint=Button(root, height=1, width=10, text="print",
                    command=lambda: retrieve_input())

buttonCommit.pack()

trie = TrieTree()
trie.printF()
mainloop()

print("TextVal",textRec)
