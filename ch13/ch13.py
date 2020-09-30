# -*- encoding: utf-8 -*-
'''
@File    :   ch13.py
@Time    :   2020/09/25 21:56:01
@Author  :   zqp 
@Version :   1.0
@Contact :   zhangqipeng@buaa.edu.cn
'''

class Node():
    def __init__(self, key):
        self.key = key
        self.color = None
        self.parent = None
        self.left = None
        self.right = None
    
    def __str__(self):  # 实现print(Node)
        return str(self.key)


class RedBlackTree():
    def __init__(self, root):
        self.root = root
        self.none = Node(None)
    
    def left_rotate(self, x):
        y = x.right  # 找到x的右孩子结点y

        x.right = y.left  # 将y的左孩子连接到x
        if y.left != self.none:
            y.left.parent = x  # y的左孩子连接到x（双向连接）

        y.parent = x.parent  # y换到x的位置
        if x.parent == self.none:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y
    
        y.left = x  # x连接到y
        x.parent = y


    def right_rotate(self, x):
        y = x.left

        x.left = y.right
        if y.right != self.none:
            y.right.parent = x
        
        y.parent = x.parent
        if x.parent == self.none:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.right = x
        x.parent = y

    