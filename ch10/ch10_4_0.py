'''
date: 2019/12/19
author: zqp111
正文10.3 二叉树
'''

class Node(object):
    def __init__(self, key, p=None, left=None, right=None):
        self.p = p
        self.left = left
        self.right = right
        self.key = key
    
    def __str__(self):
        return str(self.key)
    

class Tree(object):
    def __init__(self, root=None):
        self.root = root
    
    
        
        