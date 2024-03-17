#Aditi Saha Ria
#Id 20101238
#Sec 13
#TASK 01

class Stack:
    stack = []
    pointer = -1
    def push(self, element):
        self.stack.append(element)
        self.pointer += 1
    def peek(self):
        return(self.stack[self.pointer])
    def pop(self):
        value = self.stack[self.pointer]
        self.stack = self.stack[:-1]
        self.pointer -= 1
        return value


stack = Stack()

a = '1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'

count = 0
error = 0
for i in range(len(a)):
    if ord(a[i]) == 40 or ord(a[i]) == 123 or ord(a[i]) == 91:
        stack.push(a[i])
        count = count + 1
    elif ord(a[i]) == 41:
        if count == 0:
            print('This expression is NOT correct.')
            print(f"Error at character # {i}. ‘{a[i]}‘- not opened.")
            error = 1
            break
        elif ord(stack.peek()) == 40:
            stack.pop()
            count = count - 1
        else:
            print('This expression is NOT correct.')
            print(f"Error at character # {i}. ‘{a[i]}‘- not closed.")
            error = 1
            break
    elif ord(a[i]) == 125:
        if count == 0:
            print('This expression is NOT correct.')
            print(f"Error at character # {i}. ‘{a[i]}‘- not opened.")
            error = 1
            break
        elif ord(stack.peek()) == 123:
            stack.pop()
            count = count - 1

        else:
            print('This expression is NOT correct.')
            print(f"Error at character # {i}. ‘{a[i]}‘- not closed.")
            error = 1
            break
    elif ord(a[i]) == 93:
        if count == 0:
            print('This expression is NOT correct.')
            print(f"Error at character # {i}. ‘{a[i]}‘- not opened(.")
            error = 1
            break
        elif ord(stack.peek()) == 91:
            stack.pop()
            count = count - 1

        else:
            print('This expression is NOT correct.')
            print(f"Error at character # {i}. ‘{a[i]}‘- not closed.")
            error = 1
            break

if error == 0:
    print('This expression is correct.')