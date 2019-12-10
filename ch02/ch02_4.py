'''
date: 2019/12/10
author: zqp111
思考题 2-4 逆序对
'''

def getInversion(inputArray):   # 遍历算法
    out = []
    for i, num in enumerate(inputArray):
        for j in range(i+1, len(inputArray)):
            print(i, j)
            if num > inputArray[j]:
                out.append((i, j))
    return out

def MergeGetInver(inputArray):  # 递归算法
    L = len(inputArray)
    if L <= 1:
        return inputArray, 0
    q = L // 2
    inputArray[:q], m = MergeGetInver(inputArray[:q])
    inputArray[q:], n = MergeGetInver(inputArray[q:])
    inputArray, num = Merge(inputArray, q)
    num += n+m
    return inputArray, num

def Merge(inputArray, q):
    A = inputArray.copy()
    num = 0
    j = 0
    k = 0
    L = len(inputArray)
    for i in range(L):
        if j == q:
            inputArray[i] = A[q+k]
            k += 1
            continue
        elif k == L - q:
            inputArray[i] = A[j]
            j += 1
            continue
        
        if A[j] > A[q+k]:
            inputArray[i] = A[j]
            j += 1
            num += L -q -k
        else:
            inputArray[i] = A[q+k]
            k += 1
    return inputArray, num

if __name__ == '__main__':
    a = [5, 4, 3, 2, 1, 0]
    _, ans = MergeGetInver(a)
    print(ans)