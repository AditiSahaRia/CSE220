#Aditi Saha Ria
#ID: 20101238
#Task_04

class Node:
    def __init__(self, element, n=None):
        self.element = element
        self.next = n

class MyList:

    def __init__(self, array=None):

        if array == None:
            self.head = None

        elif isinstance(array, list):
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

    def selection_sort(self):

        tail = self.head
        count = 0
        copy = 0

        while tail.next != None:
            tail = tail.next
            count += 1

        while copy < count:
            max = self.head.element
            max_node = self.head
            tail = self.head.next
            find = 0
            while tail  is not None and find<count-copy:
                if tail.element > max:
                    max = tail.element
                    max_node = tail
                tail = tail.next
                find += 1

            if max_node == self.head and copy == 0:

                self.head = self.head.next
                tail = self.head
                while tail.next.next is not None:
                    tail = tail.next
                new_head = tail.next
                tail.next = max_node
                tail = tail.next
                tail.next = None
                new_head.next = self.head
                self.head = new_head

            else:

                tail = self.head

                while tail.next is not max_node and tail is not max_node:
                    tail = tail.next

                if tail is max_node:
                    hold = tail.next
                else:
                    hold = tail.next.next
                find = 0
                new = self.head

                while find < count-copy and new is not None:
                    new = new.next
                    find += 1

                if new == hold:
                    pre = new.next
                    max_node.next = pre

                    if tail is not max_node:
                        tail.next = new
                        new.next = max_node

                    elif tail is max_node and count-copy == 1:
                        hold.next = max_node
                        self.head = hold

                else:

                    another = tail

                    while another.next is not new:
                        another = another.next

                    another.next = max_node
                    pre = new.next
                    max_node.next = pre
                    new.next = hold
                    if tail is not  max_node:
                        tail.next = new
                    else:
                        self.head = new

            copy += 1

a = [10, 5, 9, 8, 3, 7, 4]
b = MyList(a)
b.selection_sort()
b.showList()
a = [10, 5, 4, 8]
b = MyList(a)
b.selection_sort()
b.showList()