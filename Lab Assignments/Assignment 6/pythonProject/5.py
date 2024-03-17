#Aditi Saha Ria
#ID: 20101238
#Task_05

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

    def showlist(self):
        if self.head.next == self.head:
            print('Empty List')
        else:
            tail = self.head
            while tail.next is not None:
                print(tail.val, end='<=>')
                tail = tail.next
            print(tail.val)

    def sorted(self, head, node):
        if head == None:
            head = node
        elif head.val>=node.val:
            node.next = head
            node.next.prev = node
            head = node
        else:
            tail = head
            while tail.next != None and tail.next.val<node.val:
                tail = tail.next
            node.next = tail.next
            node.prev = tail
        self.head = head
        return self.head

    def insertion_sort(self):
        in_sort = None
        tail = self.head
        while tail is not None:
            new = tail.next
            tail.next = tail.prev = None
            in_sort = sorted(in_sort, tail)
            tail = new
        self.head = in_sort


arr = [50,40,30,20,10]
b = DoublyList(arr)
b.insertion_sort()
b.showlist()