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
    def removeKey(self, deleteKey):
        copy = self.head.next
        count = 0
        while copy is not self.head:
            count += 1
            copy = copy.next
        print(count)
        for i in range(count):
            tail = self.head.next
            new = None
            if tail is None:
                return self.head
            else:
                while tail != self.head and tail.val != deleteKey:
                    new = tail
                    tail = tail.next
                if new is None:
                    n = self.head.next
                    self.head.next = n.next
                    n.next.prev = self.head
                    n.next = None
                    n.prev = None
                    print('n->', n.val)
                else:
                    new.next = tail.next
                    tail.next.prev = new
                    tail.next = None
                    tail.prev = None

        return self.head


arr = [10,20,50,40,80]
lt = DoublyList(arr)
lt.showlist()
lt.removeKey(50)
lt.showlist()