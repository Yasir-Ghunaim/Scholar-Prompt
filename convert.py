
class Converter:
    def __init__(self):
        self.filename = None
        self.convertTo = None
        self.data = None

    def newFile(self, filename):
        self.filename = filename
        f = open(self.filename, 'r')
        self.data = f.read()
        f.close()
        
    def converter(self, convertTo):
        self.convertTo = convertTo
        

    def asciiToBin(self):
        return "implementing"

    def getOriginalData(self):
        return self.data

c = Converter()
c.newFile('sample.txt')
print c.getOriginalData()


