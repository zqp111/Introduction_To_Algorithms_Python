'''
date: 2019/12/10
author: zqp111
正文和课后习题2-1-2 插入排序
'''


def InsertSort(inputArray, order='UP'):
    temp = inputArray.copy()    # 防止改变原数列
    for i, num in enumerate(temp[1:], start=1):
        j = i-1
        while j >=0 and (temp[j] > num if order.upper() == 'UP' 
                         else (temp[j] < num if order.upper() == 'DOWN' 
                         else False)):
            temp[j+1] = temp[j]
            j -= 1
        temp[j+1] = num
    
    return temp

if __name__ == "__main__":
    A = [1, 2, 4, 3]
    B = InsertSort(A,'up')
    print(A)
    print(B)
