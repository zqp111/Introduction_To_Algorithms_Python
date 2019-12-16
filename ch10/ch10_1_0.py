'''
date: 2019/12/16
author: zqp111
正文10.1 基本数据类型, 队列和栈可以由list直接实现，这里只实现双端队列
习题10.1-5 双端队列
'''

class deque(list):
    def __init__(self, iterable):
        super().__init__(iterable)

    def appendleft(self, x):
        self.insert(0, x)
    
    def popleft(self):
        assert not self.isEmpty() , "underflow"
        return self.pop(0)
    
    def isEmpty(self):
        if len(self):
            return False 
        return True
    

    
if __name__ == "__main__":
    a = deque((1,2,3))
    a.appendleft(4)
    print(a)
    a.pop()
    print(a)
    b = a.popleft()
    print(b)

    print(a.isEmpty())