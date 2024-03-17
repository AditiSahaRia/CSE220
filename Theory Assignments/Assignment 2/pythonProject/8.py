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
        #box = Node(None, None, None)
        #box.next = self.head
        #self.head.prev = box
        #self.head = box
        tail.next = self.head
        self.head.prev = tail

    def showlist(self):
        if self.head.next == self.head:
            print('Empty List')
        else:
            tail = self.head
            while tail.next is not self.head:
                print(tail.val, end='<=>')
                tail = tail.next
            print(tail.val, end='<=>')
            print(tail.next.val)

    def frydayFun(self, s):
        tail = self.head
        for i in s:
            if int(i)==2 or int(i)==4:
                copy = tail.next
                x = tail.prev
                x.next = copy
                tail.next = None
                tail.prev = None
            else:
                tail = tail.next

player = 3
sequence = '152'
arr = [0]*player
for i in range(player):
    arr[i] = i+1
lt = DoublyList(arr)
print('Showing the Dummy Headed Doubly Linked List:')
lt.showlist()