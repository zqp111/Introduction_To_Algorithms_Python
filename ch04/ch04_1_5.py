'''
date: 2019/12/11
author: zqp111
思考题 4.1-5 最大子数组 非递归算法
'''

def getMaxArray(inputArray):
    start = 0
    end = 0
    max = inputArray[0]
    sum = inputArray[0]
    for i in range(1, len(inputArray)):
        if sum < 0:
            sum = 0
            start = i
        sum += inputArray[i]
        if sum > max:
            max = sum
            end = i
        
    return start, end, max


if __name__ == "__main__":
    a = [-10,2,3,4,-5,6]
    b = getMaxArray(a)
    print(b)