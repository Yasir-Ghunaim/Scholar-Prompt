#!/usr/local/bin/python
import sys
from Gui import Gui
from Convert import Converter
from PyQt4 import QtGui

def main():
	converter = Converter()
	parseArguments(converter)

# =================================
# parse the given arguments and handle them
# =================================
def parseArguments(converter):
	if len(sys.argv) == 2:
		if sys.argv[1] == "-h":
			printHelp()
		elif sys.argv[1] == "-g":
			startGui(converter)
		# invalid argument
		else:
			printHelp()
	#elif len(sys.argv) == 3:
		#if you want add things here to handle 2 arguments
	
	# wrong number of arguments
	else:
		printHelp()

# =================================
# print available arguments
# =================================
def printHelp():
	print ""
	print "Usage: python main.py [OPTION...]\n"
	print "	-h	help"
	print "	-g	GUI"
	print ""

# =================================
# launch GUI
# =================================	
def startGui(converter):
	app = QtGui.QApplication(sys.argv)
	ex = Gui(converter)
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
