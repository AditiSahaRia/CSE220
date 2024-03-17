class Node:
    def __init__(self, element, n=None):
        self.element = element
        self.next = n
class MyList:

    def __init__(self, array):

        head = None
        tail = None
        for i in array:
            box = Node(i, None)
            if head == None:
                head = box
                tail = box
            else:
                tail.next = box
                tail = tail.next
        self.head = head
        tail.next = self.head


    def showList(self):
        if self.head == None:
            print('Empty List')
        else:
            print(self.head.element, end=' ')
            value = self.head.next
            while value != self.head:
                print(value.element, end=' ')
                value = value.next
            print(value.element)
    def insert(self, newElement, index=None):
        inserted_value = Node(newElement, None)
        copy_tail = self.head
        for i in range(index - 1):
            copy_tail = copy_tail.next
        pre = copy_tail
        inserted_value.next = pre.next
        pre.next = inserted_value

        return self.head

arr = [10,201,30]
a = MyList(arr)
a.insert(4,2)
a.showList()
