'''
date: 2019/12/10
author: zqp111
正文和2-3-2 Merge sort
'''

def MergeSort(inputArray):
    L = len(inputArray)
    if L <= 1:
        return inputArray
    q = L // 2
    inputArray[:q] = MergeSort(inputArray[:q])
    inputArray[q:] = MergeSort(inputArray[q:])
    Merge(inputArray, q)
    return inputArray

def Merge(inputArray, q):
    A = inputArray.copy()
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
        
        if A[j] < A[q+k]:
            inputArray[i] = A[j]
            j += 1
        else:
            inputArray[i] = A[q+k]
            k += 1

if __name__ == "__main__":
    a = [2,4,6,3,1,3,6,9,7,5,3,7,31,56,3,34,67,8,4]
    MergeSort(a)
    print(a)
