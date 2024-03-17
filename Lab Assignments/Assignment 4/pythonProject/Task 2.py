#Aditi Saha Ria
#Id 20101238
#Sec 13
#TASK 02

class Node:
    def __init__(self, value):
        self.value = value
        self.ref = None
class Stack:
    head = None
    ch_head = None
    def push(self, data, char):
        if self.head == None:
            self.head = Node(data)
        else:
            n = Node(data)
            n.ref = self.head
            self.head = n
        if self.ch_head == None:
            self.ch_head = Node(char+1)
        else:
            n = Node(char+1)
            n.ref = self.ch_head
            self.ch_head = n
    def peek(self):
        return self.head.value
    def ch_peek(self):
        return self.ch_head.value
    def pop(self):
        temp = self.head
        self.head = self.head.ref
        temp.value = None
        temp.ref = None
        temp = self.ch_head
        self.ch_head = self.ch_head.ref
        temp.value = None
        temp.ref = None

def balance(a):
    count = 0
    error = 0
    stack = Stack()
    for i in range(len(a)):
        if ord(a[i]) == 40 or ord(a[i]) == 123 or ord(a[i]) == 91:
            stack.push(a[i],i)
            count = count + 1
        elif ord(a[i]) == 41:
            if count == 0:
                print('This expression is NOT correct.')
                print(f"Error at character # {i+1}. ‘{a[i]}‘- not opened.")
                error = 1
                break
            elif ord(stack.peek()) == 40:
                stack.pop()
                count = count - 1
            else:
                print('This expression is NOT correct.')
                print(f"Error at character # {i+1}. ‘{stack.peek()}‘- not closed.")
                error = 1
                break
        elif ord(a[i]) == 125:
            if count == 0:
                print('This expression is NOT correct.')
                print(f"Error at character # {stack.ch_peek()}. ‘{a[i]}‘- not opened.")
                error = 1
                break
            elif ord(stack.peek()) == 123:
                stack.pop()
                count = count - 1

            else:
                print('This expression is NOT correct.')
                print(f"Error at character # {stack.ch_peek()}. ‘{stack.peek()}‘- not closed.")
                error = 1
                break
        elif ord(a[i]) == 93:
            if count == 0:
                print('This expression is NOT correct.')
                print(f"Error at character # {i+1}. ‘{a[i]}‘- not opened.")
                error = 1
                break
            elif ord(stack.peek()) == 91:
                stack.pop()
                count = count - 1

            else:
                print('This expression is NOT correct.')
                print(f"Error at character # {stack.ch_peek()}. ‘{stack.peek()}‘- not closed.")
                error = 1
                break

    if error == 0 and count == 0:
        print('This expression is correct.')
    elif error == 0 and count>0:
        print('This expression is NOT correct.')
        print(f"Error at character # {stack.ch_peek()}. ‘{stack.peek()}‘- not closed.")

frst = '1+2*(3/4)'
print(frst)
balance(frst)
print()

scnd = '1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'
print(scnd)
balance(scnd)
print()

third = '1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14'
print(third)
balance(third)
print()

fourth = '1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'
print(fourth)
balance(fourth)
print()

a = '()('
print(a)
balance(a)