class Node:
    def __init__(self, element, n=None):
        self.element = element
        self.next = n
class MyList:

    def __init__(self, array1, array2):

        first_head = None
        tail_01 = None
        for i in array1:
            box = Node(i, None)
            if first_head == None:
                first_head = box
                tail_01 = box
            else:
                tail_01.next = box
                tail_01 = tail_01.next
        n = Node(None, None)
        n.next = first_head
        self.first_head = n
        scnd_head = None
        tail_02 = None
        for i in array2:
            box = Node(i, None)
            if scnd_head == None:
                scnd_head = box
                tail_02 = box
            else:
                tail_02.next = box
                tail_02 = tail_02.next
        n = Node(None, None)
        n.next = scnd_head
        self.scnd_head = n

    def showList(self):
        value = self.first_head
        while value != None:
            print(value.element, end=' ')
            value = value.next
        print()
        value = self.scnd_head
        while value != None:
            print(value.element, end=' ')
            value = value.next
        print()

    def sum(self):
        a = self.first_head.next
        b = self.scnd_head.next
        count1 = 0
        count2 = 0
        while a is not None:
            count1 += 1
            a = a.next
        a = self.first_head.next
        while b is not None:
            count2 += 1
            b = b.next
        b = self.scnd_head.next
        r1 = 0
        while a is not None:
            r1 = r1 + a.element*(10**(count1-1))
            count1 = count1-1
            a = a.next
        r2 = 0
        while b is not None:
            r2 = r2 + b.element*(10**(count2-1))
            count2 = count2-1
            b = b.next

        add = r1+r2
        print(add)

arr1 = [1,2,3]
arr2 = [3,4,5,6,6]
a = MyList(arr1,arr2)
a.showList()
a.sum()