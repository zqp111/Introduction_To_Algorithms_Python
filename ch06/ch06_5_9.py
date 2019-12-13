'''
date: 2019/12/12
author: zqp111
习题6.5-9 合并k个有序链表(升序链表)
'''
# TODO 链表合并


from ch06 import heapSort
import random
from ch06_5_3 import buildMinHeap


def mergeArray(arrayList):
    k = len(arrayList)
    pass




if __name__ == "__main__":

    # 生成测试数据
    a = []
    b = []
    c = []
    random.seed(2)
    for i in range(10):
        a.append(random.randint(0, 99))
        b.append(random.randint(0, 99))
        c.append(random.randint(0, 99))
    heapSort(a)
    heapSort(b)
    heapSort(c)
    print(a,b,c)

