'''
date: 2019/12/12
author: zqp111
习题 5.1-2 习题5.1-3
'''
import random

def randomInt(a, b):    # 基本思想利用多次二分投掷来二进制编码 
    L = b - a + 1   # 总数
    num = 0
    while L > 0:
        L = L >> 1
        num += 1
        if L == 1:
            break   # 2的幂
    
    L = b - a + 1
    while True:
        sum = 0
        for _ in range(num):
            tmp = random.randint(0, 1)
            sum = (sum << 1)+ tmp
        if sum <= L:
            break
    
    return a + sum


def randomBin():     # 基本思想,利用不平等随机数产生两次,通过出现0,1的先后次序作为等概率随机数
    while True:
        sum = 0
        for _ in range(2):
            tmp = random.randint(0, 1)
            sum = (sum << 1) + tmp
        if sum == 1 or sum == 2:    # 这两种情况概率均为p(1-p)
            return sum -1




if __name__ == "__main__":
    print(randomInt(2,9))
    print(randomBin())
