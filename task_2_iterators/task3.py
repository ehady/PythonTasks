def generateOddNumbers():
    value = 1
    while True:
        yield value
        value += 2


for i in generateOddNumbers():
    print(i)