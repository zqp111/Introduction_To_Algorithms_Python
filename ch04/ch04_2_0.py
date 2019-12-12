'''
date: 2019/12/11
author: zqp111
正文 4.2 矩阵乘法的Strassen算法 仅包含2幂情况
'''
import numpy as np


def matMul(matA, matB):
    arow, aline = matA.shape
    if arow == 1:
        return np.array([[matA[0, 0]*matB[0, 0]]])

    C = np.zeros((arow,aline))

    p = arow >> 1

    s1 = matB[:p, p:] - matB[p:, p:]
    s2 = matA[:p, :p] + matA[:p, p:]
    s3 = matA[p:, :p] + matA[p:, p:]
    s4 = matB[p:, :p] - matB[:p, :p]
    s5 = matA[:p, :p] + matA[p:, p:]
    s6 = matB[:p, :p] + matB[p:, p:]
    s7 = matA[:p, p:] - matA[p:, p:]
    s8 = matB[p:, :p] + matB[p:, p:]
    s9 = matA[:p, :p] - matA[p:, :p]
    s10 = matB[:p, :p] + matB[:p, p:]

    p1 = matMul(matA[:p, :p], s1)
    p2 = matMul(s2, matB[p:, p:])
    p3 = matMul(s3, matB[:p, :p])
    p4 = matMul(matA[p:, p:], s4)
    p5 = matMul(s5, s6)
    p6 = matMul(s7, s8)
    p7 = matMul(s9, s10)

    C[:p, :p] = p5 + p4 - p2 + p6
    C[:p, p:] = p1 + p2
    C[p:, :p] = p3 + p4
    C[p:, p:] = p5 + p1 - p3 - p7
    return C


if __name__ == "__main__":
    a = np.array([[1, 3], [7, 5]])
    b = np.array([[6, 8], [4, 2]])
    c = matMul(a, b)
    print(c)
