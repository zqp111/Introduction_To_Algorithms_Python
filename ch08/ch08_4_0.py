'''
date: 2019/12/15
author: zqp111
正文8.4 桶排序
习题8.2-4, 顺便回答了8.2-3
'''
import random
import sys
sys.path.append("..")
from ch02.ch02_1_0 import InsertSort

def bucketSort(inputArray):
    n = len(inputArray)
    b = [[] for _ in inputArray]
    for i in range(n):
        b[int(n * inputArray[i])].append(inputArray[i])

    c = []  # 输出缓存

    for lis in b:
        InsertSort(lis)
        c += lis        # 连接列表
    return c


if __name__ == "__main__":
    a = []
    for _ in range(10):
        a.append(random.random())
    print(a)
    b = bucketSort(a)
    print(b)