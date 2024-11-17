from Dictionary import Dictionary

def testDictionary():
    print("*** Testing Dictionary")
    d = Dictionary()
    d.newentry("Apple","A fruit that grows on trees")
    print(d.look("Apple"))
    print(d.look("Banana"))

def totalCost(items,tax):
    costs = {'socks': 5, 'shoes': 60, 'sweater': 30}
    total = 0
    for item in items:
        if item in costs:
            total += costs[item]
    return total+total*tax

def testTotalCost():
    print("*** Testing totalCost")
    print(totalCost(['socks','shoes'],0.09))

def word(words):
    newWord = ""
    for i,word in enumerate(words):
        newWord += word[i]
    return newWord

def testWord():
    print("*** Testing word")
    print(word(["yoda", "best","has"]))

def __main__():
    testDictionary()
    testTotalCost()
    testWord()

if __name__ == "__main__":
    __main__()