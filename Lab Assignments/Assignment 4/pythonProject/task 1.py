#Aditi Saha Ria
#Id 20101238
#Sec 13
#TASK 01

class Stack:
    stack = []
    ch_stack = []
    pointer = -1
    index = 0
    ch_index = 0
    def length(self, n):
        self.stack = ['']*n
        self.ch_stack = ['']*n
    def push(self, element, char):
        self.stack[self.index] = (element)
        self.ch_stack[self.ch_index] = char+1
        self.pointer += 1
        self.index += 1
        self.ch_index += 1
    def peek(self):
        return(self.stack[self.pointer])
    def ch_peek(self):
        return  self.ch_stack[self.pointer]
    def pop(self):
        value = self.stack[self.pointer]
        self.stack = self.stack[:-1]
        #ch_value = self.ch_stack[self.pointer]
        self.ch_stack = self.ch_stack[:-1]
        self.pointer -= 1
        return value


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
                print(f"Error at character # {i+1}. ‘{a[i]}‘- not opened(.")
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
    else:
        print('This expression is NOT correct.')


ar = '()('#'1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14'
balance(ar)

array = '('#'1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'
#balance(array)