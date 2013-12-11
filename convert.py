def converter(file, toType):
    f = open(file, 'r')
    char = f.read(1);
    print("==================== %s",char)
    p = f.read()
    print p
    print f
    f.close()

def asciiToBin(file):
    print "implementing"