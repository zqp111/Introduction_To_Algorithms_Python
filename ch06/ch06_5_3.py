'''
date: 2019/12/12
author: zqp111
习题6.5-3 最小优先队列
'''
import random

parent = lambda i : ((i+1) >> 1) -1
left = lambda i : (i << 1) +1
right  = lambda i : (i << 1) + 2

min = lambda i : i[0]

def minHeapify(inputArray, i):      # 递归算法
    l = left(i)
    r = right(i)
    if l < inputArray[-1] and inputArray[l] < inputArray[i]:
        minindex = l
    else:
        minindex = i
    
    if r < inputArray[-1] and inputArray[r] < inputArray[minindex]:
        minindex = r
    
    if minindex != i:   # 交换根叶节点, 继而需要维护被交换的叶节点 
        inputArray[i], inputArray[minindex] = inputArray[minindex], inputArray[i]
        minHeapify(inputArray, minindex)

def buildMinHeap(inputArray):
    inputArray.append(len(inputArray))
    for i in range(inputArray[-1]>> 1, -1, -1):   # 自下向上维护各個子樹, 从而生成一个最大堆
        minHeapify(inputArray, i)
    inputArray.pop(-1)

def heapSortMin(inputArray):
    buildMinHeap(inputArray)
    inputArray.append(len(inputArray))
    for i in range(inputArray[-1]-1, 0, -1):
        inputArray[i], inputArray[0] = inputArray[0], inputArray[i]
        inputArray[-1] -= 1
        minHeapify(inputArray, 0)
    inputArray.pop(-1)


def extraxtMin(inputArray):
    assert len(inputArray) > 0, "empty array"
    min = inputArray[0]
    inputArray[0] = inputArray[-1]
    inputArray.pop(-1)
    inputArray.append(len(inputArray))
    minHeapify(inputArray, 0)
    inputArray.pop(-1)
    return min

def decreaseKey(inputArray, i, key):
    assert i < len(inputArray), "out of index"
    assert inputArray[i] > key, "new is bigger than current key"

    # inputArray[i] = key    

    while i > 0 and inputArray[parent(i)] > key:
        # inputArray[parent(i)], inputArray[i] = inputArray[i], inputArray[parent(i)]
        inputArray[i] = inputArray[parent(i)]
        i = parent(i)

    inputArray[i] = key

def insertKey(inputArray, key):
    i = len(inputArray)
    inputArray.append(float("inf"))
    decreaseKey(inputArray, i, key)



if __name__ == "__main__":
    a = []
    for _ in range(10):
        a.append(random.randint(0,99))
    
    buildMinHeap(a)
    print(a)

    insertKey(a, 78)
    print(a)

    decreaseKey(a, 10, 1)
    print(a)

    extraxtMin(a)
    print(a)
