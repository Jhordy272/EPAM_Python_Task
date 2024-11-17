from Dictionary import Dictionary

def testDictionary():
    print("*** Testing Dictionary")
    d = Dictionary()
    d.newentry("Apple","A fruit that grows on trees")
    print(d.look("Apple"))
    print(d.look("Banana"))

def __main__():
    testDictionary()

if __name__ == "__main__":
    __main__()