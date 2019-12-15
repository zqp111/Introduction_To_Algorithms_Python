'''
date: 2019/12/10
author: zqp111
正文和课后习题2-1-2 插入排序
'''
import random

def InsertSort(inputArray, order='UP'):
    for i, num in enumerate(inputArray[1:], start=1):
        j = i-1
        while j >=0 and (inputArray[j] > num if order.upper() == 'UP' 
                         else (inputArray[j] < num if order.upper() == 'DOWN' 
                         else False)):
            inputArray[j+1] = inputArray[j]
            j -= 1
        inputArray[j+1] = num
    
    return inputArray

if __name__ == "__main__":
    a = []
    for _ in range(10):
        a.append(random.randint(0, 99))
    InsertSort(a,'up')
    print(a)
