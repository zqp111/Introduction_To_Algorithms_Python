'''
date: 2019/12/12
author: zqp111
正文第六章 最大优先队列
习题6.5-6, 6.5-8
'''

from ch06 import buildMaxHeap, maxHeapify, parent
import random

max = lambda i : i[0]

def extraxtMax(inputArray):
    assert len(inputArray) > 0, "empty array"
    max = inputArray[0]
    inputArray[0] = inputArray[-1]
    inputArray.pop(-1)
    inputArray.append(len(inputArray))
    maxHeapify(inputArray, 0)
    inputArray.pop(-1)
    return max


def increaseKey(inputArray, i, key):
    assert i < len(inputArray), "out of index"
    assert inputArray[i] < key, "new is smaller than current key"

    # inputArray[i] = key    

    while i > 0 and inputArray[parent(i)] < key:
        # inputArray[parent(i)], inputArray[i] = inputArray[i], inputArray[parent(i)]
        inputArray[i] = inputArray[parent(i)]
        i = parent(i)

    inputArray[i] = key


def insertKey(inputArray, key):
    i = len(inputArray)
    inputArray.append(float("-inf"))
    increaseKey(inputArray, i, key)

def deleteKey(inputArray, i):
    assert i < len(inputArray), "out of index"
    increaseKey(inputArray, i, float("inf"))
    extraxtMax(inputArray)


if __name__ == "__main__":
    a = []
    random.seed(2)
    for _ in range(10):
        a.append(random.randint(0,99))
    print(a)
    a.append(len(a))
    buildMaxHeap(a)
    a.pop(-1)
    print(a)

    insertKey(a, 78)
    print(a)

    increaseKey(a, 1, 600)
    print(a)

    extraxtMax(a)
    print(a)

    deleteKey(a, 2)
    print(a)

