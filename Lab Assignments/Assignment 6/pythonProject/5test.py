# Python3 implementation for insertion Sort
# on a doubly linked list

# Node of a doubly linked list
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# function to create and return a new node
# of a doubly linked list
def getNode(data):
    # allocate node
    newNode = Node(0)

    # put in the data
    newNode.data = data
    newNode.prev = newNode.next = None
    return newNode
# function to insert a new node in sorted way in
# a sorted doubly linked list
def sortedInsert(head_ref, newNode):
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
def insertionSort(head_ref):
    # Initialize 'sorted' - a sorted
    # doubly linked list
    sorted = None

    # Traverse the given doubly linked list
    # and insert every node to 'sorted'
    current = head_ref
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
    head_ref = sorted

    return head_ref


# function to print the doubly linked list
def printList(head):
    while (head != None):
        print(head.data, end=" ")
        head = head.next


# function to insert a node at the
# beginning of the doubly linked list
def push(head_ref, new_data):
    """ allocate node """
    new_node = Node(0)

    """ put in the data """
    new_node.data = new_data

    """ Make next of new node as head
    and previous as None """
    new_node.next = (head_ref)
    new_node.prev = None

    """ change prev of head node to new node """
    if ((head_ref) != None):
        (head_ref).prev = new_node

    """ move the head to point to the new node """
    (head_ref) = new_node
    return head_ref


# Driver Code
if __name__ == "__main__":
    """ start with the empty doubly linked list """
    head = None

    # insert the following data
    head = push(head, 9)
    head = push(head, 3)
    head = push(head, 5)
    head = push(head, 10)
    head = push(head, 12)
    head = push(head, 8)

    print("Doubly Linked List Before Sorting")
    printList(head)

    head = insertionSort(head)

    print("\nDoubly Linked List After Sorting")
    printList(head)

# This code is contributed by Arnab Kundu
