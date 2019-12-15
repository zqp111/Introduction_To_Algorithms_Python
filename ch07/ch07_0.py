'''
date: 2019/12/15
author: zqp111
正文第7章, 快速排序,随机化版本, 
习题7.1-2
'''
import random

def quickSort(inputArray, p, r):
    if r - p <= 1:
        return
    q = split(inputArray, p, r, True)
    quickSort(inputArray, p, q)
    quickSort(inputArray, q+1, r)

def split(inputArray, p, r, randmo = False):
    if random:
        midindex = random.randint(p, r-1)
        inputArray[midindex], inputArray[r-1] = inputArray[r-1], inputArray[midindex]

    mid = inputArray[r-1]
    i = p
    flag = True           # 保证在q左右两边分配尽量相等个数的中值
    for j in range(p, r-1):
        if inputArray[j] < mid:
            inputArray[i], inputArray[j] = inputArray[j], inputArray[i]
            i += 1
        elif inputArray[j] == mid:
            if flag:
                inputArray[i], inputArray[j] = inputArray[j], inputArray[i]
                i += 1
                flag = False
            else:
                flag = True
    inputArray[i], inputArray[r-1] = inputArray[r - 1], inputArray[i]
    return i
    

if __name__ == "__main__":
    a = []
    for _ in range(10):
        a.append(random.randint(0, 99))
    quickSort(a, 0, 10)
    print(a)

    # 验证等值数列在调用split时返回中间索(习题7.1-2)
    b = [1 for i in range(10)]
    q = split(b, 0, 10)
    print(q)