import string
import os
import sys

def enum(**enums):
    return type('Enum', (), enums)

class Converter:
    def __init__(self):
        self.filename = None
        self.data = None
        self.dataType = None
        self.DataType = enum(ASCII='ASCII', Binary='BINARY', Hex='HEX')
        
    # =================================
    # takes the file that is to be converted
    # =================================
    def newFile(self, filename):
        self.filename = filename
        f = open(self.filename, 'r')
        self.data = f.read()
        f.close()
        #check data type
        self.detectType(self.data)
        
    # =================================
    # detects the type of file's content
    # =================================
    def detectType(self, data):
        self.dataType = self.DataType.ASCII
        #binary detection
        if all((c in set('01')) for c in self.data):
            self.dataType = self.DataType.BINARY
        #hex detection
        elif all((c in string.hexdigits) for c in self.data):
            self.dataType = self.DataType.HEX
    # =================================
    # takes the type to convert to and returns the converted data
    # =================================
    def convertTo(self, filename, convertTo):
        f = open(filename, 'r')
        value = 'invalid parameter'
        ct = convertTo.lower()
        ct = ct.replace(' ', '')
        if ct == 'asciitobinary':
            value = self.asciiToBinary(f)
        elif ct == 'binarytoascii':
            value = self.binToAscii(f)
        elif ct == 'binarytohex':
            value = self.binToHex(f)
        elif ct == 'hextobinary':
            value = self.hexToBin(f)
        elif ct == 'asciitohex':
            value = self.asciiToHex(f)
        elif ct == 'hextoascii':
            value = self.hexToAscii(f)
        f.close()
        return value
        
    # =================================
    # converters
    # =================================
    def asciiToBinary(self, fString):
        value = ''
        if fString != sys.stdin:
            fString.seek(0)
        while 1:
            char = fString.read(1)
            if not char: break
            char = ord(char) 
            strg = ''.join('01'[(char >> x) & 1] for x in xrange(7, -1, -1))
            sys.stdout.write(strg)  
            value += str(strg)
        print ""
        return value

    def binToAscii(self, fString):
        value = ''
        if fString != sys.stdin:
            fString.seek(0,2)
            flength = fString.tell()
            fString.seek(0)
        else:
            flength = 8
        try:
            for i in range(0, flength/8):
                char = fString.read(8)
                if not char: break
                strg = (chr(int(char, 2)))
                sys.stdout.write(strg)
                value += str(strg)  
            print ""
        except:
            print 'Given input was not proper binary'
            value = 'Given input was not proper binary'
        return value

    def binToHex(self, fString):
        value = ''
        if fString != sys.stdin:
            fString.seek(0,2)
            flength = fString.tell()
            fString.seek(0)
        else:
            flength = 4
        try:
            for i in range(0, flength/4):
                char = fString.read(4)
                if not char: break
                strg = (hex(int(char, 2)))[2:]
                sys.stdout.write(strg)
                value += str(strg)
            print ""
        except:
            print 'Given input was not proper binary'
            value = 'Given input was not proper binary'
        return value

    def hexToBin(self, fString):
        value = ''
        if fString != sys.stdin:
            fString.seek(0,2)
            flength = fString.tell()
            fString.seek(0)
        else:
            flength = 1
        try:
            for i in range(1, flength):
                char = fString.read(1)
                if not char: break
                strg = (bin(int(char, 16)))[2:]
                strg = -len(strg)%4*'0'+strg
                sys.stdout.write(strg)
                value += str(strg)
            print ""
        except:
            print 'Given input was not proper binary'
            value = 'Given input was not proper binary'
        return value

    def asciiToHex(self, fString):
        value = ''
        if fString != sys.stdin:
           fString.seek(0)

        # convert to bin, store in temp file
        file = "temp"
        tempFile = open(file, 'w+')
        if fString != sys.stdin:
           fString.seek(0)
        while 1:
            char = fString.read(1)
            if not char: break
            char = ord(char) 
            strg = ''.join('01'[(char >> x) & 1] for x in xrange(7, -1, -1))
            tempFile.write(strg)

        flength = tempFile.tell()
        tempFile.seek(0)

        # convert to hex
        for i in range(0, flength/4):
            char = tempFile.read(4)
            if not char: break
            strg = (hex(int(char, 2)))[2:]
            sys.stdout.write(strg)
            value += str(strg)
        print ""
        os.remove("./temp")
        return value

    def hexToAscii(self, fString):
        value = ''
        # convert hex to bin and store in temp file
        try:
            if fString != sys.stdin:
                fString.seek(0,2)
                flength = fString.tell()
                fString.seek(0)
            else:
                flength = 4
            file = "temp"
            tempFile = open(file, 'w+')

            for i in range(1, flength):
                char = fString.read(1)
                if not char: break
                strg = (bin(int(char, 16)))[2:]
                strg = -len(strg)%4*'0'+strg
                tempFile.write(strg)

            flength = tempFile.tell()
            tempFile.seek(0)
            #convert bin file to ascii
            for i in range(0, flength/8):
                char = tempFile.read(8)
                if not char: break
                strg = (chr(int(char, 2)))
                strg = strg.replace('\n', '') # TODO FIX THIS
                sys.stdout.write(strg)
                value += str(strg)
            print ""
            os.remove("./temp")
        except:
            print 'Given input was not proper hex'
            value = 'Given input was not proper hex'
        return value



