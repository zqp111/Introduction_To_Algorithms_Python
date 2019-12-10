'''
date: 2019/12/10
author: zqp111
课后习题2-1-4 二进制加法
'''

def BinAdd(numA, numB):
    # numA和numB都是高位排在数组的前面 例[1, 1, 0, 1] = 13
    if len(numA) > len(numB):
        for _ in range(len(numA)- len(numB)):
            numB.insert(0,0)
    elif len(numA) < len(numB):
        for _ in range(len(numB)- len(numA)):
            numA.insert(0,0)
    print(len(numA), len(numB))
    ans = []
    c = 0   # 进位
    for a, b in zip(reversed(numA), reversed(numB)):
        c, out = bitAdd(a, b, c)
        ans.insert(0, out)
    if c:
        ans.insert(0, c)
    return ans

def bitAdd(a, b, c):    # 单位二进制加法
    out = (a ^ b) ^ c
    c = (a & b) | ((a ^ b) & c)
    return c, out


if __name__ == "__main__":
    a = [1, 0, 0, 1, 0]
    b = [1, 1, 1, 1]
    ans = BinAdd(a, b)  
    print(ans)