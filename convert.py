
class Converter:
    def __init__(self):
        self.filename = None
        self.data = None

    # =================================
    # takes the file that is to be converted
    # =================================
    def newFile(self, filename):
        self.filename = filename
        f = open(self.filename, 'r')
        self.data = f.read()
        f.close()
        
    # =================================
    # takes the type to convert to and returns the converted data
    # =================================
    def convertTo(self, convertTo):
        value = 'invalid parameter'
        ct = convertTo.lower()
        ct = ct.replace(' ', '')
        if ct == 'asciitobinary':
            value = self.asciiToBinary(self.data)
        elif ct == 'binarytoascii':
            value = self.binToAscii(self.data)
        elif ct == 'binarytohex':
            value = self.binToHex(self.data)
        elif ct == 'hextobinary':
            value = self.hexToBin(self.data)
        elif ct == 'asciitohex':
            value = self.asciiToBinary(self.data)
            value = self.binToHex(value)
        elif ct == 'hextoascii':
            value = self.hexToBin(self.data)
            value = self.binToAscii(value)
        return value

    # =================================
    # converters
    # =================================
    def asciiToBinary(self, string):
        binary = bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in string), 0))
        return binary[2:]

    def binToAscii(self, string):
        #TODO: prevent from non ascii file
        #if len(self.data)%8 == 0:
        bitstring = string
        bitstring = -len(bitstring) % 8 * '0' + bitstring
        string_blocks = (bitstring[i:i+8] for i in range(0, len(bitstring), 8))
        strg = ''.join(chr(int(char, 2)) for char in string_blocks)
        return strg

    def binToHex(self, string):
        h = hex(int(string, 2))[2:-1]
        hblock = (h[i:i+2] for i in range(0, len(h), 2))
        h = ''.join((char + ' ') for char in hblock)
        return h

    def hexToBin(self, string):
        b = string.replace(' ', '')
        return bin(int(b, 16))[2:]