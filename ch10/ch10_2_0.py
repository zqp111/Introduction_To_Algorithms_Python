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
    
    def __str__(self):  # 便于显示
        return str(self.key)



class linkedList(object):
    def  __init__(self, head = None):
        self.head = head
    
    def __len__(self):
        x = self.head
        length = 0
        while x != None:
            length += 1
            x = x.next
        return length

    def search(self, key):
        x = self.head
        while x.key != key:
            x = x.next
        return x
    
    def insert(self, x):    # 前插入
        x.next = self.head
        if self.head != None:
            self.head.prov = x
        self.head = x
        x.prov = None
    
    def append(self, x):    # 后插入
        if self.head == None:
            self.head = x
            x.prov = None
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = x
            x.prov = cur
        x.next = None
    
    def delete(self, x):
        if x.prov != None:  # 不是链表头
            x.prov.next = x.next
        else:
            self.head = x.next
        if x.next != None:
            x.next.prov = x.prov

    
if __name__ == "__main__":
    l = linkedList()
    a1 = Node(1)
    a2 = Node(2)
    l.append(a1)
    print(l.head)
    l.insert(a2)
    print(l.head)
    print(l.search(1))
    l.delete(l.search(1))
    print(l.head)