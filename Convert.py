import string

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
			self.dataType = DataType.HEX
		#temporary print datatype
		print self.dataType
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
		try:
			binary = bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in string), 0))
			binary = binary[2:]
		except:
			binary = 'Given input was not proper ASCII'
		return binary

	def binToAscii(self, string):
		try:
			#TODO: prevent from non ascii file
			#if len(self.data)%8 == 0:
			bitstring = string
			bitstring = -len(bitstring) % 8 * '0' + bitstring
			string_blocks = (bitstring[i:i+8] for i in range(0, len(bitstring), 8))
			strg = ''.join(chr(int(char, 2)) for char in string_blocks)
		except:
			strg = 'Given input was not proper binary'
		return strg

	def binToHex(self, string):
		try:
			h = hex(int(string, 2))[2:-1]
			hblock = (h[i:i+2] for i in range(0, len(h), 2))
			h = ''.join((char + ' ') for char in hblock)
		except:
			h = 'Given input was not proper binary'
		return h

	def hexToBin(self, string):
		try:
			b = string.replace(' ', '')
			b = bin(int(b, 16))[2:]
		except:
			b = 'Given input was not proper hex'
		return b
