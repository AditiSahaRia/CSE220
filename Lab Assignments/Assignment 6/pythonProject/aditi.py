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

    def insertion_sort(self):
        tail = self.head
        count = 0
        while tail is not None:
            tail = tail.next
            count = count + 1
        i = 1

        while i < count:
            j = i-1
            key = self.head
            l = 0
            while l<i and key != None:
                key = key.next
                l += 1
            temp = self.head
            l = 0
            while l<j and temp != None:
                temp = temp.next
                l += 1
            while j >=0 and key.val<temp.val:
                temp.next = temp
                j = j-1

            temp.next = key
            i += 1


arr = [50,40,30,20,10]
b = DoublyList(arr)
b.insertion_sort()
b.showlist()
