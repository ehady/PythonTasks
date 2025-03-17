class evenRange:
    def __init__(self, start, end):
        self.value = start if start % 2 == 0 else start - 1
        self.stop = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            print("Out of numbers!")
            raise StopIteration
        self.value += 2
        return self.value



for n in evenRange(1,10):
    print(n)

