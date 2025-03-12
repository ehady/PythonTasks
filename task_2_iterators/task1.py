class mySquareIterator:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, item):
        return self.items[item] ** 2



iterable_1 = mySquareIterator([1,2,3,4])

for i in iterable_1:
    print(i)