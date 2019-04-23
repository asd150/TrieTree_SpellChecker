
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QColor, QPen, QTextCursor

from trietree_GUI import Ui_MainWindow  # importing our generated file

from backend_demo import *

import sys


class mywindow(QtWidgets.QMainWindow):


    def __init__(self):
        super(mywindow, self).__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.buttonInitial.clicked.connect(self.trie_generate)

        self.ui.buttonCheck.clicked.connect(self.spellCheck)

        self.ui.actionOpen.triggered.connect(self.openTxt)

        self.ui.actionImport.triggered.connect(self.importDic)

        self.txt = ""

    def importDic(self):
        path, type = QtWidgets.QFileDialog.getOpenFileName(self, "open file")
        file = open(path, 'r')
        with file:
            dict = file.read()

    def openTxt(self):
        path, type = QtWidgets.QFileDialog.getOpenFileName(self, "open file")
        with open(path, 'r') as file:
            self.txt = file.read()
        self.ui.textInput.setText(self.txt)

    def trie_generate(self):
        self.ui.labelTitle.setText(build_tree())

    def spellCheck(self):
        self.txt = self.ui.textInput.toPlainText()
        error_marker, marked_txt, recom = check_error(self.txt)
        if error_marker:
            self.ui.labelCheck.setText("Errors detected")
        else:
            self.ui.labelCheck.setText("No problem")
        self.ui.textInput.setText(marked_txt)
        self.ui.textOutput.setText(recom)


app = QtWidgets.QApplication([])

application = mywindow()

application.show()

sys.exit(app.exec())