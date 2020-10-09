# -*- encoding: utf-8 -*-
'''
@File    :   ch15_2.py
@Time    :   2020/10/09 15:08:07
@Author  :   zqp 
@Version :   1.0
@Contact :   zhangqipeng@buaa.edu.cn
'''


import numpy as np

class matrixChainMultiplication():
    def __init__(self, matrixChain):
        '''
        args: 
            matrixChain: numpy array 2*n
        '''
        self.matrixChain = matrixChain
        self.l = self.matrixChain.shape[1]
        self.m = np.zeros((self.l, self.l))
        self.result = np.zeros((self.l, self.l))
    
    def solve(self):
        for length in range(2, self.l+1): # 链长度，2--n
            for i in range(self.l -length+1):
                j = i + length -1
                self.m[i, j]=np.inf
                for k in range(i, j):
                    q = self.m[i, k]+self.m[k+1, j]+self.matrixChain[0, i]*self.matrixChain[1, k]*self.matrixChain[1, j]
                    if q < self.m[i, j]:
                        print(length)
                        self.m[i, j] = q
                        self.result[i, j] = k


if __name__ == "__main__":
    matrixChain = np.array([[10, 100, 5],
                   [100, 5, 50]
                    ])
    print(matrixChain.shape)
    a = matrixChainMultiplication(matrixChain)
    a.solve()
    print(a.m[0, 2])
