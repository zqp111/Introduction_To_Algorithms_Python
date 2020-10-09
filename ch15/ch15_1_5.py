# -*- encoding: utf-8 -*-
'''
@File    :   ch15_1_5.py
@Time    :   2020/09/30 19:52:17
@Author  :   zqp 
@Version :   1.0
@Contact :   zhangqipeng@buaa.edu.cn
'''
import numpy as np

def get_fibonacci(n):

    def __get_fibonacci(n, r):
        if r[n] >= 0:
            return r[n]
        return __get_fibonacci(n-1, r)+ __get_fibonacci(n-2, r)
    r = np.array([i if i<2  else -1 for i in range(n+1)], dtype=np.int32)
    return __get_fibonacci(n, r)


if __name__ == '__main__':
    for i in range(10):
        print(get_fibonacci(i))