# -*- encoding: utf-8 -*-
'''
@File    :   ch15_4.py
@Time    :   2020/10/09 16:39:06
@Author  :   zqp 
@Version :   1.0
@Contact :   zhangqipeng@buaa.edu.cn
'''

import numpy as np

class LCS():
    def __init__(self, X, Y):
        '''
            args: 
                X: numpy array N
                Y: numpy array M
        '''
        self.X = X
        self.Y = Y
        self.c = np.zeros((X.shape[0], Y.shape[0]), dtype=np.int32)
        self.Z = list()
    
    def solve(self):
        

        def solve_r(X, Y):
            if self.c[X.shape[0]-1, Y.shape[0]-1] >= 0:
                return self.c[X.shape[0]-1, Y.shape[0]-1]
            if X.shape[0] == 0 or Y.shape[0] == 0:
                return 0
            if X[-1] == Y[-1]:
                print('eq', end=' ')
                q = solve_r(X[:-1], Y[:-1]) +1
            else:
                q = max(solve_r(X[:-1], Y), solve_r(X, Y[:-1]))
            print(X.shape[0]-1, Y.shape[0]-1, q)
            self.c[X.shape[0]-1, Y.shape[0]-1] = q
            return q

        self.c -= 1
        solve_r(self.X, self.Y)
        self.getZ()

    def getZ(self):
        i = self.X.shape[0] -1
        j = self.Y.shape[0] -1 
        while i != -1 and j != -1 and self.c[i, j]!= 0:
            if i -1 <0:
                self.Z.insert(0, self.X[i])
                i -= 1
            elif j -1 <0:
                self.Z.insert(0, self.X[i])
                j -=1
            elif self.c[i, j] != self.c[i-1,j] and self.c[i,j] != self.c[i, j-1]:
                self.Z.insert(0, self.X[i])
                i -= 1
                j -= 1
            elif self.c[i, j] == self.c[i-1, j]:
                i -= 1
            else:
                j -= 1
                pass
        
if __name__ == "__main__":
    # A = np.array(['y','h','a', 'b', 'f', 'z', 'c'])
    # B = np.array(['h', 'g','a', 'd', 'b', 'm', 'z', 'j', 'o', 'q', 'c'])
    A = np.array([1])
    print(A[:-1].shape)
    A = np.random.randint(5, size=5)
    B = np.random.randint(5, size=5)
    A = np.array([4, 1, 3, 3, 1])
    B = np.array([4, 1, 1, 0, 2])
    print(A, B)
    a = LCS(A, B)
    a.solve()
    print(a.c)
    print(a.Z)
