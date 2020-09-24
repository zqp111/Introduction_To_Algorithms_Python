'''
date: 2019/12/19
author: zqp111
正文10.3 二叉树
'''

class Node(object):
    def __init__(self, key, index, p=None, left=None, right=None):
        self.p = p
        self.left = left
        self.right = right
        self.key = key
        self.index = index # 建树时方便使用表来建立
    
    def __str__(self):
        return str(self.key)
    

class Tree(object):
    def __init__(self, table, root=None):
        self.root = Node(table[root, 0], root)
        self.table = table
    

    def buildTree(self):


    def __buildTree(self, status):
        node = self.table[status.index]
        if not node[1] and not node[2]:
            return
        if node[1] != None:
            status.left = Node(self.table[node[1], 0], node[1])
        if node[2] != None:
            status.right = Node(self.table[node[2],0], node[2])
            


    
    
        
        