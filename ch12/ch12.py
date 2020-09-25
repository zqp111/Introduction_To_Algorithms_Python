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

    def transplant(self,u,v):
        '''
        parameter: 
            u: 待替代树结点
            v: 要替代树结点
        '''
        if u == self.root:
            self.root = v
        if u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent
    
    def delete(self,z):
        '''Delete
        parameter: 
            z: 待删除结点
        '''
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = z.right
            while y.left != None:
                y = y.left
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y


if __name__ == "__main__":
    root = Node(11)
    key_list = [4, 7, 1, 9, 20, 2, 5, 10, 3, 0, -12, 30, 8]
    node_list = list()
    tree = SearchTree(root)
    for i in key_list:
        node_list.append(Node(i))
        tree.insert(node_list[-1])
    
    m = tree.search(8)
    min_ = tree.minimize_re()
    max_ = tree.maximize()
    # print(min_, max_)

    tree.delete(node_list[2])

    tree.tree_walk()
    print(tree.tree_key, len(tree))