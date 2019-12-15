'''
date: 2019/12/15
author: zqp111
习题7.4-5
'''


import sys
sys.path.append('..')
from ch02.ch02_1_0 import InsertSort
from ch07_0 import split
import random

k = 8

def quickSort2(inputArray, p, r):
    if r - p <= k:
        return
    q = split(inputArray, p, r, True)
    quickSort2(inputArray, p, q)
    quickSort2(inputArray, q+1, r)
    if r - q <= 2*k +1:
        insert(inputArray, p, r)


def insert(inputArray, p, r):
    inputArray[p:r] = InsertSort(inputArray[p :r])


if __name__ == "__main__":
    a = []
    for _ in range(10):
        a.append(random.randint(0, 99))
    
    quickSort2(a, 0, 10)
    print(a)