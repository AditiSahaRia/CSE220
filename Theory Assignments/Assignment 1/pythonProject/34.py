class Node:
    def __init__(self, data, next, prev):
        self.data=data
        self.next=next
        self.prev=prev


class  Mylist:
    def __init__(self, lst= None):
        self.head=Node(None,None,None)
        self.head.next=self.head.prev=self.head
        temp=self.head

        if type(lst)==list:
            for i in lst:
                n= Node(i,None,None)
                temp.next=n
                n.prev=temp
                n.next=self.head
                self.head.prev=n
                temp=temp.next

    def showList(self):
        l=self.head
        while True:
            print(l.data)
            if l.next is self.head:
                break
            l=l.next
    def insertBefore(self,elem, newElement):
        node=Node(newElement,None,None)
        temp=self.head.next
        while True:
            if temp.data==elem:
                temp.prev.next=node
                node.prev=temp.prev
                node.next=temp
                temp.prev=node
            if temp.next is self.head:
                break
            temp=temp.next

lst=[4,5,3]
a=Mylist(lst)
#a.insert(6,3)

a.insertBefore(5,6)
a.showList()