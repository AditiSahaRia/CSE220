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

    def sortedInsert(self, head_ref, newNode):
        current = None

        # if list is empty
        if (head_ref == None):
            head_ref = newNode

        # if the node is to be inserted at the beginning
        # of the doubly linked list
        elif ((head_ref).data >= newNode.data):
            newNode.next = head_ref
            newNode.next.prev = newNode
            head_ref = newNode

        else:
            current = head_ref

            # locate the node after which the new node
            # is to be inserted
            while (current.next != None and
                   current.next.data < newNode.data):
                current = current.next

            """Make the appropriate links """
            newNode.next = current.next

            # if the new node is not inserted
            # at the end of the list
            if (current.next != None):
                newNode.next.prev = newNode

            current.next = newNode
            newNode.prev = current

        return head_ref;

    # function to sort a doubly linked list
    # using insertion sort
    def insertionSort(self):
        # Initialize 'sorted' - a sorted
        # doubly linked list
        sorted = None

        # Traverse the given doubly linked list
        # and insert every node to 'sorted'
        current = self.head
        while (current != None):
            # Store next for next iteration
            next = current.next

            # removing all the links so as to create
            # 'current' as a new node for insertion
            current.prev = current.next = None

            # insert current in 'sorted' doubly linked list
            sorted = sortedInsert(sorted, current)

            # Update current
            current = next

        # Update head_ref to point to
        # sorted doubly linked list
        self.head = sorted

        return self.head


arr = [50,40,30,20,10]
b = DoublyList(arr)
b.showlist()