#Aditi Saha Ria
#ID: 20101238
#Task_05

class Node:
    def __init__(self, val, n, p):
        self.data = val
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
                print(tail.data, end='<=>')
                tail = tail.next
            print(tail.data)

    def insertion_sort(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        index = 1
        temp = self.head
        while index < count:
            if temp == self.head:
                temp = temp.next
                continue
            temp2 = temp
            while temp is not self.head:
                if temp.data >= temp.prev.data:
                    break
                else:
                    a = temp.prev.data
                    temp.prev.data = temp.data
                    temp.data = a
                    temp = temp.prev
            temp = temp2
            temp = temp.next
            index = index + 1

arr = [50,40,30,20,10]
b = DoublyList(arr)
b.insertion_sort()
b.showlist()