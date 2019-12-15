'''
date: 2019/12/15
author: zqp111
正文8.2 计数排序
习题8.2-4, 顺便回答了8.2-3
'''

import random

def countSort(inputArray, k):
    c = [0 for _ in range(k)]
    for num in inputArray:
        c[num] = c[num] + 1

    for i in range(1, k):   # 现C中储存着每个数的排序 
        c[i] += c[i -1] 
    
    b = [0 for _ in range(len(inputArray))]

    for num in inputArray:  # 算法非稳定的,即相等的数值排序后其位置会发生变化, 使用倒序即可保证算法是稳定的
        b[c[num]-1] = num
        c[num] -= 1

    return b

def countArray(inputArray, k):
    c = [0 for _ in range(k)]
    for num in inputArray:
        c[num] = c[num] + 1

    for i in range(1, k):   # 现C中储存着每个数的排序 
        c[i] += c[i -1] 
    return c

def getCount(inputArray, a, b, k):  #  返回a, b 之间的数的个数(包含a, b),习题8.2-4
    assert a <= b, "a is smaller than b"
    c = countArray(inputArray, k)
    return c[b] - c[a -1]


if __name__ == "__main__":
    a = []
    random.seed(2)
    for _ in range(10):
        a.append(random.randint(0, 20))
    print(a)
    b = countSort(a, 21)
    print(b)
    count = getCount(a, 2,5,21)
    print(count)