def converter(file, toType):
    f = open(file, 'r')
    f.read()
    print f

if __name__ == "__main__":
    converter('sample.txt', 'hex')