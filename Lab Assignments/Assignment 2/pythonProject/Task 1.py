#Task_01
#i

class Node:

    def __init__(self, object, node):
        # object - variable used to store the value

        # node_class - variable used to reference to link to the next node
        self.data = object

        self.next = node


class MyList:
    def __init__(self, a):
        self.head = None
        tail = None
        for i in a:
            n = Node(i,None)
            if(self.head==None):
                self.head = n
                tail = n
            else:
                tail.next = n
                tail = n

    def printlist(self):
        node = self.head
        if(self.head is None):
            print('No element')
        while(node != None ):
            print(node.data)
            node = node.next

class MyList1:

    def __init__(self,otherList=None):
        self.head = None
        self.tail = None

        if type(otherList) == list:
            pass
        ## Constructor for array/list
        elif type(otherList) == MyList1:
            pass
        ## Existing list
class MyList2:
    def __init__(self,a=None):
        if a==None:
            return
            #create an empty List
        elif isinstance(a, list):
            pass
            #if array is given
        elif isinstance(a, MyList2):
            pass
            #if MyList type of data is given
        else:
            print("Wrong datatype passed in the constructor so creating an empty MyList")
            #create an empty List

class MyList3:
    def __init__(self,a=None):
        if a==None:
            pass
            #create an empty List
        elif isinstance(a, list):
            pass
            #if array is given
        elif isinstance(a, MyList):
            pass
            #if MyList type of data is given
        else:
            print("Wrong datatype passed in the constructor so creating an empty MyList")
            #create an empty List



arr = [10,20,30,40,50]
list1 = MyList(arr)
list1.printlist()