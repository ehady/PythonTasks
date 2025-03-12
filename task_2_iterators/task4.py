def generateFibonacci(end):
    cur_val = 0
    nex_val = 1
    while cur_val < end:
        yield  nex_val
        temp, cur_val = cur_val, nex_val
        nex_val += temp


for i in generateFibonacci(34):
    print(i)

