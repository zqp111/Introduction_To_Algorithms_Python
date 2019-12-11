'''
date: 2019/12/10
author: zqp111
课后习题2-1-3 查找元素
'''

def Search(inputArray, key):
    index = []
    for i, num in enumerate(inputArray):
        if num == key:
            index.append(i)
    if index == []:
        return None
    return index

if __name__ == "__main__":
    A = [1, 2, 4, 3]
    B = Search(A, 5)
    print(B)
    