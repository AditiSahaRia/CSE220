class Node:
    def __init__(self, element, n=None):
        self.element = element
        self.next = n
def nodeAt(head, size, index):

    if(index<0 or index>=size):

        return None

    n = head

    for i in range(0,index):

        n = n.next

    return n

#remove function

def sort(self):
    tail = self.head
    li = []

    while tail != None:
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