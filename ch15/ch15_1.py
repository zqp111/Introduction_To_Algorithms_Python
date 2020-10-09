# -*- encoding: utf-8 -*-
'''
@File    :   ch15_1.py
@Time    :   2020/09/30 11:02:23
@Author  :   zqp 
@Version :   1.0
@Contact :   zhangqipeng@buaa.edu.cn
@fuction :   正文15.1, 练习15.1.4
'''
import numpy as np

class CutRod():
    def __init__(self,length, p):
        self.length = length
        self.p = p
    
    def bottom_up_solve(self):
        r = np.zeros(self.length+1, dtype=np.int32)
        s = np.zeros(self.length+1, dtype=np.int32)
        for i in range(1, self.length+1):
            q = -1
            for j in range(1, i+1):
                # q = max(q, self.p[j]+r[i-j])
                if q < self.p[j]+r[i-j]:
                    q = self.p[j]+r[i-j]
                    s[i] = j
            r[i] = q
        # return r[-1]
        return r, s


    def up_bottom_solve(self):

        def solve(p, r, n):
            if r[n] >= 0:  # 已存在，查表
                return r[n]
            q = -1
            for i in range(1, n+1):
                # q = max(q, p[i]+solve(self.p, r, n-i))
                if q < p[i]+solve(self.p, r, n-i):
                    q = p[i]+solve(self.p, r, n-i)
                    s[n] = i
            r[n] = q  # 保存表
            return r[n]


        r= np.array([-1 for i in range(self.length+1)], dtype=np.int32)
        s = np.zeros(self.length+1, dtype=np.int32)
        r[0] = 0
        return solve(self.p, r, self.length), s
        
            
    def get_split(self,s):
        result = []
        n = self.length
        while n != 0:
            result.append(s[n])
            n = n - s[n]
        return result


if __name__ == '__main__':
    p = np.array([0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30])
    for i in range(1, 11):
        a = CutRod(i, p)
        # print(a.bottom_up_solve(), a.up_bottom_solve())
        r, s = a.up_bottom_solve()
        print(i, r, a.get_split(s))
