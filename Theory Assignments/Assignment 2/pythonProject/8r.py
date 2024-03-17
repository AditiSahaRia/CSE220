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
        if self.head.next == self.head:
            print('Empty List')
        else:
            tail = self.head
            while tail.next is not self.head:
                print(tail.val, end='<=>')
                tail = tail.next
            print(tail.val)


    def insert(self, newElement, index=None):
        box = Node(newElement, None, None)
        if index==None:
            if self.head.next is None:
                self.head.next = box
                box.prev = self.head
            else:
                tail = self.head.next
                while tail.next is not self.head:
                    tail = tail.next
                tail.next = box
                tail.next.prev = tail
                tail = tail.next
                tail.next = self.head
                self.head.prev = tail

        else:
            tail = self.head.next
            for i in range(index-1):
                tail = tail.next
            pre = tail
            box.next = pre.next
            pre.next.prev = box
            box.prev = pre
            pre.next = box

    def remove(self, index):
        tail = self.head.next
        copy_tail = self.head.next
        count = 0
        while copy_tail.next is not self.head:
            count += 1
            copy_tail = copy_tail.next
        print(count)
        if index<0 or index>count:
            raise Exception("Invalid index")
        remove_val = None
        if index==0:
            tail = self.head

        else:
            for i in range(index - 1):
                tail = tail.next
        remove_val = tail.next
        tail.next = remove_val.next
        remove_val.next.prev = tail
        remove_val.next = None
        remove_val.prev = None
        return remove_val.val

    def removeKey(self, deleteKey):
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
            else:
                new.next = tail.next
                tail.next.prev = new
                tail.next = None
                tail.prev = None
        return tail.val


arr = [10,20,30,40]
lt = DoublyList(arr)
print('Showing the Dummy Headed Doubly Linked List:')
lt.showlist()
lt.insert(80)
print('After insertion showing the Dummy Headed Doubly Linked List:')
lt.showlist()
print(f'Removed value -> {lt.remove(1)}')
print('After removal showing the Dummy Headed Doubly Linked List:')
lt.showlist()
print(f'Delet Key -> {lt.removeKey(10)}')
print('After removing deletKey showing the Dummy Headed Doubly Linked List:')
lt.showlist()
