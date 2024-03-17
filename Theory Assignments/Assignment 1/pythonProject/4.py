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

    def showList(self):
        if self.head == None:
            print('Empty List')
        else:
            value = self.head
            while value != None:
                print(value.element, end=' ')
                value = value.next
            print()

    def change_head(self, m):
        tail = self.head
        new = None
        for i in range(m):
            new = tail
            tail = tail.next
        new_head = tail
        new.next = None
        while tail.next is not None:
            tail = tail.next
        tail.next = self.head
        self.head = new_head
        return self.head
    def remove(self,m):
        n = None
        if m==0:
            n = self.head
            self.head = self.head.next
        else:
            tail = self.head
            for i in range(m-1):
                tail = tail.next
            pre = tail
            rem = pre.next
            pre.next = rem.next
        rem.element = None
        rem.next = None
        return self.head

    def printDuplicate(self):
        tail = self.head
        while tail is not None:
            n = tail.next
            while n is not None:
                if n.element is tail.element:
                    print(n.element)

                    return
                else:
                    n = n.next
            tail = tail.next

    def remove_multiple_of_five(self):
        n = self.head
        while n is not None:
            tail = self.head
            new = None

            while tail is not None and tail.element%5!=0:
                new = tail
                tail = tail.next
            if new is None:
                self.head = tail.next
                n = self.head
            elif tail is None:
                new.next = None
            else:
                new.next = tail.next
            n = n.next
        if n is None and self.head.element%5==0:
            self.head = None

        return self.head
    def insert(self, newElement, index=None):
        inserted_value = Node(newElement, None)
        if index==None:
            if self.head==None:
                self.head = inserted_value
            else:
                tail = self.head
                while(tail.next != None):
                    tail = tail.next
                tail.next = inserted_value
                #tail = tail.next
        elif index==0:
            inserted_value.next = self.head
            self.head = inserted_value
        else:
            copy_tail = self.head
            for i in range(index-1):
                copy_tail = copy_tail.next
            pre = copy_tail
            inserted_value.next = pre.next
            pre.next = inserted_value
        return self.head

arr = [10,201,30]
a = MyList(arr)
a.remove(1)
#a.change_head(2)
#a.printDuplicate()
#a.remove_multiple_of_five()
a.showList()
#a.remove_multiple_of_five()