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
    # standard input
    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            printHelp()
        elif sys.argv[1] == "-g":
            startGui(converter)
        elif sys.argv[1] == "-ab":
            converter.asciiToBinary(sys.stdin)
        elif sys.argv[1] == "-ba":
            converter.binToAscii(sys.stdin)
        elif sys.argv[1] == "-ax":
            converter.asciiToHex(sys.stdin)
        elif sys.argv[1] == "-xa":
            converter.hexToAscii(sys.stdin)
        elif sys.argv[1] == "-bx":
            converter.binToHex(sys.stdin)
        elif sys.argv[1] == "-xb":
            converter.hexToBin(sys.stdin)
        else:
            printHelp()

    # file input
    elif len(sys.argv) > 2:
        fcount = len(sys.argv) - 2
        if sys.argv[1] == "-h":
            printHelp()
        elif sys.argv[1] == "-g":
            startGui(converter)
        elif sys.argv[1] == "-ab":
            for f in range(0, fcount):
                converter.convertTo(sys.argv[2+f], 'asciitobinary')
        elif sys.argv[1] == "-ba":
            for f in range(0, fcount):
                converter.convertTo(sys.argv[2+f], 'binarytoascii')
        elif sys.argv[1] == "-bx":
            for f in range(0, fcount):
                converter.convertTo(sys.argv[2+f], 'binarytohex')
        elif sys.argv[1] == "-xb":
            for f in range(0, fcount):
                converter.convertTo(sys.argv[2+f], 'hextobinary')
        elif sys.argv[1] == "-ax":
            for f in range(0, fcount):
                converter.convertTo(sys.argv[2+f], 'asciitohex')
        elif sys.argv[1] == "-xa":
            for f in range(0, fcount):
                converter.convertTo(sys.argv[2+f], 'hextoascii')
        else:
            printHelp()
    
    
    # wrong number of arguments
    else:
        printHelp()

# =================================
# print available arguments
# =================================
def printHelp():
    print ""
    print "Usage: python main.py [CONVERTER] [File ...]\n"
    print " -h  help"
    print " -g  GUI"
    print ""
    print " CONVERTERS:"
    print "   -ab ASCII to Binary"
    print "   -ba Binary to ASCII"
    print "   -ax ASCII to Hex"
    print "   -xa Hex to ASCII"
    print "   -bx Binary to Hex"
    print "   -xb Hex to Binary"
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
