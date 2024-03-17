class Node:
    def __init__(self, element, n=None):
        self.element = element
        self.next = n
class MyList:

    def __init__(self, array=None):
        #task_2 --> 1a
        if array==None:
            self.head = None
        # task_2 --> 1b
        elif isinstance(array,list):
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
        # task_2 --> 1c
        elif isinstance(array, MyList):
            copyHead = None

            copyTail = None

            n = array.head

            while n != None:

                newNode = Node(n.element, None)

                if copyHead == None:

                    copyHead = newNode

                    copyTail = newNode

                else:

                    copyTail.next = newNode

                    copyTail = copyTail.next

                n = n.next
            self.head = copyHead

    # task_2 --> 2
    def showList(self):
        if self.head == None:
            print('Empty List')
        else:
            value = self.head
            while value != None:
                print(value.element, end=' ')
                value = value.next
            print()

    # task_2 --> 3
    def isEmpty(self):
        return self.head is None

    # task_2 --> 4
    def clear(self):
        self.head = None

    # task_2 --> 5 and 6
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

    # task_2 --> 7
    def remove(self, deletekey):
        tail = self.head
        new = None
        while tail != None and tail.element!= deletekey:
            new = tail
            tail = tail.next
        new.next = tail.next
        return self.head

    # task_3 --> 1
    def evenNumbers(self):
        tail = self.head

        while (tail != None):
            if tail.element%2==0:
                print(tail.element, end='->')
            tail = tail.next
        print()

    # task_3 --> 2
    def find_element(self, value):
        result = False
        tail = self.head
        while tail!=None:
            if tail.element==value:
                result = True
            tail = tail.next
        print(result)
    # task_3 --> 3
    def reverse(self):
        newHead = None

        n = self.head

        while (n != None):
            nextNode = n.next

            n.next = newHead

            newHead = n

            n = nextNode
        self.head = newHead
        return self.head
    # task_3 --> 4
    def sort(self):
        tail = self.head
        li = []
        while tail!=None:
            li.append(tail.element)
            tail = tail.next
        li.sort()
        head = None
        tail = None
        for i in li:
            box = Node(i, None)
            if head == None:
                head = box
                tail = box
            else:
                tail.next = box
                tail = tail.next
        self.head = head

        return self.head
    # task_3 --> 5
    def sum(self):
        add = 0
        tail = self.head
        while tail!=None:
            add += tail.element
            tail = tail.next
        print(add)
    # task_3 --> 6
    def rotate(self,position,k=1):
        tail = self.head
        if tail == None:
            print('Empty List')
            return
        elif tail.next == None:
            print(tail.element)
            return
        else:
            if position.lower()=='left':
                for i in range(k):
                    old = self.head

                    self.head = self.head.next

                    tail = self.head

                    while (tail.next != None):
                        tail = tail.next

                    tail.next = old

                    old.next = None

                return self.head

            elif position.lower()=='right':
                for i in range(k):
                    tail = self.head
                    while tail.next.next!=None:
                        tail = tail.next
                    copy_tail = tail.next
                    copy_tail.next = self.head
                    self.head = copy_tail
                    tail.next = None
                return self.head


arr = []
a = MyList(arr)
a.showList()
arr1 = [10,40,20,50,30]
b = MyList(arr1)
b.showList()
c = MyList(b)
c.showList()
print(a.isEmpty())
print(b.isEmpty())
b.clear()
b.showList()
b.insert(6)
b.showList()
b.insert(8)
b.insert(9,0)

b.showList()
c.remove(30)
c.showList()
c.evenNumbers()
c.showList()
c.find_element(20)
c.reverse()
c.showList()
c.sort()
c.showList()
c.sum()
c.rotate('left')
c.showList()
c.rotate('right',2)
c.showList()

