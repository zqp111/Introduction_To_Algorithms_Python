'''
date: 2019/12/10
author: zqp111
思考题 2-4 逆序对
'''

def GetMaxArray(inputArray, start=0, end=0, First=False):
    if First:
        end = len(inputArray)
    print(start,end)

    if end - start <= 1:
        return start, end, inputArray[start]
    mid = (end + start) //2
    Lstart, Lend, Lmax = GetMaxArray(inputArray, start, mid)
    Mstart, Mend, Mmax = GetMaxArray(inputArray, mid, end)
    Rstart, Rend, Rmax = GetMaxCross(inputArray, start, end)


def GetMaxCross(inputArray, start, end):
    mid = (start + end) // 2
    Lmax = inputArray[mid]
    Lindex = mid
    Lsum = 0
    for i in range(mid, start-1, -1):
        Lsum += inputArray[i]
        if Lsum > Lmax:
            Lmax = Lsum
            Lindex = i
    
    Rmax = inputArray[mid]
    Rindex = mid
    Rsum = 0
    for i in range(mid, end):
        Rsum += inputArray[i]
        if Rsum > Rmax:
            Rmax = Rsum
            Rindex = i
    
    max = Rmax + Lmax - inputArray[mid]
    return Lindex, Rindex,max







if __name__ == '__main__':
    a = [1,2,3,4,5,6,7]
    # b = GetMaxArray(a,First=True)
    b = GetMaxCross(a,1,3)
    print(b)