'''
date: 2019/12/15
author: zqp111
正文9.1 寻找最大最小值
'''
import random


def getMaxMin(inputArray):
    n = len(inputArray)
    if n %2:
        max = min = inputArray[0]
    else:
        if inputArray[0] > inputArray[1]:
            max = inputArray[0]
            min = inputArray[1]
        else:
            max = inputArray[1]
            min = inputArray[0]
    for i in range(n-1, 1, -2):     # 每次取两个数比较
        if inputArray[i] > inputArray[i-1]:
            if inputArray[i] > max:
                max = inputArray[i]
            if inputArray[i-1] < min:
                min = inputArray[i-1]
            
        else:
            if inputArray[i] < min:
                min = inputArray[i]
            if inputArray[i-1] > max:
                max = inputArray[i-1]
    return max, min

if __name__ == "__main__":
    a = []
    for _ in range(11):
        a.append(random.randint(0, 99))
    max, min = getMaxMin(a)
    print(a)
    print(max, min)
