class Node:
    def __init__(self, val, n, p):
        self.val = val
        self.next = n
        self.prev = p

class DoublyList:
    def __init__(self, a):
        head = None
        tail = None
        for i in a:
            box = Node(i, None, None)
            if head is None:
                head = box
                tail = box
            else:
                tail.next = box
                tail.next.prev = tail
                tail = tail.next

        self.head = head
        box = Node(None, None, None)
        box.next = self.head
        self.head.prev = box
        self.head = box
        tail.next = self.head
        self.head.prev = tail

    def showlist(self):
        if self.head.next == None:
            print('Empty List')
        else:
            tail = self.head
            while tail.next is not self.head:
                print(tail.val, end='->')
                tail = tail.next
            print(tail.val)
            while tail is not self.head:
                print(tail.val, end='->')
                tail = tail.prev
            print(tail.val)

    def insert(self, elem, newElement):
        box = Node(newElement, None, None)
        tail = self.head.next
        new = None
        while tail.val is not elem and tail is not None:
            new = tail
            tail = tail.next
        pre = new
        box.next = pre.next
        pre.next.prev = box
        box.prev = pre
        pre.next = box



        return self.head

arr = [10,20,50,40,80]
lt = DoublyList(arr)
lt.showlist()
lt.insert(40,60)
lt.showlist()