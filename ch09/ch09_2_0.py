'''
date: 2019/12/16
author: zqp111
正文9.2 寻找第i大的值
'''

import random

def split(inputArray, p, r):
    midindex = random.randint(p, r-1)
    inputArray[midindex], inputArray[r-1] = inputArray[r-1], inputArray[midindex]
    mid = inputArray[r-1]
    i = p
    for j in range(p, r-1):
        if inputArray[j] < mid:
            inputArray[i], inputArray[j] = inputArray[j], inputArray[i]
            i += 1
    inputArray[i], inputArray[r-1] = inputArray[r - 1], inputArray[i]
    return i

def select(inputArray, p, r, i):
    print(p, r, i)
    if r -p <= 0:
        return
    q = split(inputArray, p, r) 
    if q - p +1 == i:
        return inputArray[q]
    elif q - p +1 > i:
        return select(inputArray, p, q, i)
    else :
        return select(inputArray, q+1, r, i-q+p-1)

if __name__ == "__main__":
    a = []
    random.seed(2)
    for _ in range(10):
        a.append(random.randint(0, 99))
    m = select(a, 0, 10, 8)
    print(a)
    print(m)
