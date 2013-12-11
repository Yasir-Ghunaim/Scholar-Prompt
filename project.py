#!/usr/bin/python

import sys
from convert import Converter
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):      

		# open button
        self.openBtn = QtGui.QPushButton('Open', self)
        self.openBtn.move(10, 10)
        self.openBtn.clicked.connect(self.openFileButton)
        # save button
        self.saveBtn = QtGui.QPushButton('Save', self)
        self.saveBtn.move(310, 10)
        #self.saveBtn.clicked.connect(self.openFile)
        # input text edit
        self.inputTextEdit = QtGui.QTextEdit(self)
        self.inputTextEdit.move(10, 40)
        # output text edit
        self.outputTextEdit = QtGui.QTextEdit(self)
        self.outputTextEdit.move(310, 40)
        # convert button
        self.openBtn = QtGui.QPushButton('Convert', self)
        self.openBtn.move(100, 240)
        self.openBtn.clicked.connect(self.convertToButton)
        # convert to combo box
        self.convertToCombo = QtGui.QComboBox(self)
        self.convertToCombo.addItem("Binary")
        self.convertToCombo.addItem("Hex")
        self.convertToCombo.addItem("ASCII")
        self.convertToCombo.move(20, 240)
        
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Input dialog')
        self.show()
        
        self.converter = Converter()
        
    def openFileButton(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, "Open File","","Files (*.*)")
        self.converter.newFile(fileName)
        self.inputTextEdit.setText(self.converter.getOriginalData())
        
    def convertToButton(self):
		convertType = str(self.convertToCombo.currentText())
		convertedDate = self.converter.convertTo(convertType)
		self.outputTextEdit.setText(convertedDate)
		
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
