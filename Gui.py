import sys
from Convert import Converter
from PyQt4 import QtGui

class Gui(QtGui.QWidget):
	def __init__(self, converter):
		super(Gui, self).__init__()
		self.converter = converter
		self.initUI()
		
	def initUI(self):      
		#open button
		self.openBtn = QtGui.QPushButton('Open', self)
		self.openBtn.move(10, 10)
		self.openBtn.clicked.connect(self.openFileButton)
		QtGui.QShortcut(QtGui.QKeySequence("Ctrl+o"), self, self.openFileButton)
		#save button
		self.saveBtn = QtGui.QPushButton('Save', self)
		self.saveBtn.move(310, 10)
		self.saveBtn.clicked.connect(self.saveFileButton)
		QtGui.QShortcut(QtGui.QKeySequence("Ctrl+s"), self, self.saveFileButton)
		#input text edit
		self.inputTextEdit = QtGui.QTextEdit(self)
		self.inputTextEdit.move(10, 40)
		#output text edit
		self.outputTextEdit = QtGui.QTextEdit(self)
		self.outputTextEdit.move(310, 40)
		#convert button
		self.openBtn = QtGui.QPushButton('Convert', self)
		self.openBtn.move(150, 240)
		self.openBtn.clicked.connect(self.convertToButton)
		#convert to combo box
		self.convertToCombo = QtGui.QComboBox(self)
		self.convertToCombo.addItem("ASCII to Binary")
		self.convertToCombo.addItem("Binary to ASCII")
		self.convertToCombo.addItem("ASCII to Hex")
		self.convertToCombo.addItem("Hex to ASCII")
		self.convertToCombo.addItem("Binary to Hex")
		self.convertToCombo.addItem("Hex to Binary")
		self.convertToCombo.move(20, 240)
        
		#close program
		QtGui.QShortcut(QtGui.QKeySequence("Ctrl+q"), self, self.close)
		self.setGeometry(100, 100, 600, 400)
		self.setWindowTitle('Input dialog')
		self.show()
        
	def openFileButton(self):
		fileName = QtGui.QFileDialog.getOpenFileName(self, "Open File","","Files (*.*)")
		#read file and show its content in the input field
		self.converter.newFile(fileName)
		self.inputTextEdit.setText(self.converter.data)
	def saveFileButton(self):
		fileName = QtGui.QFileDialog.getSaveFileName(self, "Save file", "", ".txt")
		try:
			f = open(fileName,'w')
			f.write(str(self.outputTextEdit.toPlainText()))
			f.close()
		except:
			print 'invalid filename'
	def convertToButton(self):
		self.converter.data = str(self.inputTextEdit.toPlainText())
		convertType = str(self.convertToCombo.currentText())
		convertedDate = self.converter.convertTo(convertType)
		self.outputTextEdit.setText(convertedDate)

