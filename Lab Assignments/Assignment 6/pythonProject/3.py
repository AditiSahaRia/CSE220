#Aditi Saha Ria
#ID: 20101238
#Task_03

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
    def bubble_sort(self):

        tail = self.head
        count = 0
        copy = 0

        while tail.next != None:
            tail = tail.next
            count += 1

        while copy<=count:
            if self.head.element > self.head.next.element:
                temp = Node(self.head.next.element,None)
                self.head.next = self.head.next.next
                temp.next = self.head
                self.head = temp

            copy_tale = self.head

            while copy_tale.next != None:
                if copy_tale.next is not None and copy_tale.next.next is not None:
                    if copy_tale.next.element > copy_tale.next.next.element:
                        temp = Node(copy_tale.next.next.element, None)
                        row = copy_tale.next.next.next
                        pre = Node(copy_tale.next.element, None)
                        temp.next = pre
                        pre.next = row
                        copy_tale.next = temp
                copy_tale = copy_tale.next

            copy = copy+1


a = [5,1,3,2,4,1,4,9]
b = MyList(a)
b.bubble_sort()
b.showList()