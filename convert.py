
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
        if convertTo.lower() == 'binary':
            value = self.toBinary()
        else:
            value = 'TODO'
        return value

    # =================================
    # convert to binary
    # =================================
    def toBinary(self):
        binary = bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in self.data), 0))
        return binary[2:]

    # =================================
    # return original data
    # =================================
    def getOriginalData(self):
        return self.data

