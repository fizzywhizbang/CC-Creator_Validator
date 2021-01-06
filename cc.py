#!/usr/bin/env python3

#imports
from faker import Faker
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import uic



Ui_Gen, baseClass = uic.loadUiType('templates/creator.ui')


class CCGen(baseClass, Ui_Gen):
    """docstring for CCGen."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.genButton.clicked.connect(self.generate)
        
    def generate(self):
        #empty the text box
        # self.ccdataBox = qtw.QPlainTextEdit()
        self.ccdataBox.clear()
        cctype = self.cc_type.itemText(self.cc_type.currentIndex())
        fake = Faker('en_US')
        count = int(self.spinBox.text())
        ccdata = ""
        
        if str(cctype).lower() != "choose card type":
            for _ in range(count):
                ccdata += fake.credit_card_full(str(cctype).lower())
                ccdata += "\n"
        else:
            ccdata = "Please Choose Card Type"
        
        self.ccdataBox.setPlainText(ccdata)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = CCGen()
    mw.show()
    sys.exit(app.exec())