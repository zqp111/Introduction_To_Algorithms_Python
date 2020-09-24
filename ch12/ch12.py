# -*- encoding: utf-8 -*-
'''
@File    :   ch12.py
@Time    :   2020/09/24 15:10:27
@Author  :   zqp 
@Version :   1.0
@Contact :   zhangqipeng@buaa.edu.cn
@fuction :   正文12搜索树
'''

import numpy as np


class Node():
    def __init__(self,key, left=None, right=None, parent=None):
        self.key = key
        self.left =left
        self.right =right
        self.parent = parent

    def __str__(self):
        return str(self.key)


class SearchTree():
    def __init__(self, root):
        self.root = root


    def insert(self,insert_x):
        x = self.root
        y = None
        while x != None:
            y = x
            if insert_x.key < x.key:
                x = x.left
            else:
                x = x.right
        if insert_x.key >= y.key:
            y.right = insert_x
        else:
            y.left = insert_x
        insert_x.parent = y
    
    def tree_walk(self):
        self.tree_key = list()
        def walk(x):
            if x != None:
                walk(x.left)
                self.tree_key.append(x.key)
                walk(x.right)
        
        walk(self.root)

    def __len__(self): # 实现len方法，可以len(SearchTree)以获得节点数目
        self.tree_walk()
        return len(self.tree_key)

    def search(self,key):
        x = self.root
        while x != None:
            if key == x.key:
                return x
            elif key < x.key:
                x = x.left
            else:
                x = x.right
        return None
    
    def minimize(self):
        x = self.root
        while x.left != None:
            x = x.left
        return x
    
    def maximize(self):
        x = self.root
        while x.right != None:
            x = x.right
        return x

    def minimize_re(self): # 习题12-2.2

        def min_(x):
            if x.left == None:
                return x
            return min_(x.left)
        
        return min_(self.root)

        

    def maximize_re(self): # 习题12-2.2
        
        def max_(x):
            if x.right == None:
                return x
            return max_(x.right)
        
        return max_(self.root)




if __name__ == "__main__":
    root = Node(9)
    node1 = Node(8)
    node2 = Node(10)
    node3 = Node(1)
    node4 = Node(4)
    tree = SearchTree(root)

    tree.insert(node1)
    tree.insert(node2)
    tree.insert(node3)
    tree.insert(node4)

    m = tree.search(8)
    min_ = tree.minimize_re()
    max_ = tree.maximize()
    # print(min_, max_)

    tree.tree_walk()
    print(tree.tree_key, len(tree))