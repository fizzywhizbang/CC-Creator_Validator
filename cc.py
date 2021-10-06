#!/usr/bin/env python3

#imports
from faker import Faker
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import uic



Ui_Gen, baseClass = uic.loadUiType('creator.ui')


class CCGen(baseClass, Ui_Gen):
    """docstring for CCGen."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.genButton.clicked.connect(self.generate) 
    
    
    def generate(self):
        #empty the text box
        self.ccdataBox.clear()
        self.cctype = self.cc_type.itemText(self.cc_type.currentIndex())
        self.count = int(self.spinBox.text())
        ccdata = makeFake(self.cctype, self.count)        
        self.ccdataBox.setPlainText(ccdata)
        f = open(self.cctype + "-ccfile.txt", "w")
        f.write(ccdata)
        f.close()

def makeFake(cctype: str, count: int) -> str:
    fake = Faker()
    fake.seed_locale('en_US',2)
    ccdata = ""
    
    if str(cctype).lower() != "choose card type":
        for _ in range(count):
            ccdata += fake.credit_card_full(str(cctype).lower())
            ccdata += fake.ssn()
            ccdata += "\n"
    else:
        ccdata = "Please Choose Card Type"

    return ccdata


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = CCGen()
    mw.show()
    sys.exit(app.exec())