'''
date: 2019/12/16
author: zqp111
正文10.1 链表
'''

class Node():
    def __init__(self, key, prov=None, next=None):
        self.prov = prov
        self.next = next
        self.key = key


def searchList(List, key):
    x = List.head.copy()
    while x.key != key:
        x = x.next
    return x
