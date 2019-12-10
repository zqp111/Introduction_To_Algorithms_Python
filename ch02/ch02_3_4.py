'''
date: 2019/12/10
author: zqp111
习题2-3-4 插入排序递归版
'''

def InsertSort(inputArray):
    if len(inputArray) <= 1:
        return inputArray
    inputArray[:-1] = InsertSort(inputArray[:-1])
    inputArray = Merge(inputArray)
    return inputArray

def Merge(inputArray):
    for i, num in enumerate(inputArray):
        if num > inputArray[-1]:
            inputArray.insert(i, inputArray[-1])
            return inputArray[:-1]
    return inputArray

if __name__ == '__main__':
    a = [3,4,1,5,7,9,34,23,2,13,5,764,3,45,7,23,8]
    a = InsertSort(a)
    print(a)