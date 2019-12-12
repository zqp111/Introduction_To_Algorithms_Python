'''
date: 2019/12/12
author: zqp111
习题 4.2-7 复数乘法
'''

def complexMul(a, b, c, d):
    # 输入代表两个复数 a+bi, c+di
    s1 = a - b
    s2 = a + b
    s3 = c + d

    p1 = s1 * c
    p2 = s2 * d
    p3 = s3 * a

    real = p3 - p2
    imag = p3 - p1

    return real, imag


if __name__ == "__main__":
    r, i = complexMul(1, 2, 3, 4)
    print(r, i)
