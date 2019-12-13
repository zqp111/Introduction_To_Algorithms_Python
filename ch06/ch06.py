'''
date: 2019/12/12
author: zqp111
正文第六章 堆排序
习题6.2-5
'''
import random

parent = lambda i : ((i+1) >> 1) -1
left = lambda i : (i << 1) +1
right  = lambda i : (i << 1) + 2

def maxHeapify(inputArray, i):      # 递归算法
    l = left(i)
    r = right(i)
    if l < inputArray[-1] and inputArray[l] > inputArray[i]:
        maxindex = l
    else:
        maxindex = i
    
    if r < inputArray[-1] and inputArray[r] > inputArray[maxindex]:
        maxindex = r
    
    if maxindex != i:   # 交换根叶节点, 继而需要维护被交换的叶节点 
        inputArray[i], inputArray[maxindex] = inputArray[maxindex], inputArray[i]
        maxHeapify(inputArray, maxindex)

def maxHeapify2(inputArray, i):     # 非递归算法
    while True:
        l = left(i)
        r = right(i)
        if l < inputArray[-1] and inputArray[l] > inputArray[i]:
            maxindex = l
        else:
            maxindex = i
        
        if r < inputArray[-1] and inputArray[r] > inputArray[maxindex]:
            maxindex = r
        
        if maxindex != i:   # 交换根叶节点, 继而需要维护被交换的叶节点 
            inputArray[i], inputArray[maxindex] = inputArray[maxindex], inputArray[i]
            i = maxindex
        else:
            break


def buildMaxHeap(inputArray):
    for i in range(inputArray[-1]>> 1, -1, -1):   # 自下向上维护各個子樹, 从而生成一个最大堆
        maxHeapify2(inputArray, i)


def heapSort(inputArray):
    inputArray.append(len(inputArray))      # 以最后一位表示堆元素个数
    buildMaxHeap(inputArray)
    for i in range(inputArray[-1]-1, 0, -1):
        inputArray[i], inputArray[0] = inputArray[0], inputArray[i]
        inputArray[-1] -= 1
        maxHeapify2(inputArray, 0)
    inputArray.pop(-1)

if __name__ == "__main__":
    a = []
    for _ in range(10):
        a.append(random.randint(0,99))
    heapSort(a)
    print(a)
    