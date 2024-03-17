#Aditi Saha Ria
#ID: 20101238
#Task 01

class KeyIndex:
    def __init__(self, a):
        self.a = a
        min = 0
        max = 0

        for i in self.a:
            if i > max:
                max = i
            elif i < min:
                min = i

        if min < 0:
            min = min * (-1)

        for i in range(len(self.a)):
           self.a[i] = self.a[i]+min

        max = max+min

        self.k = [0]*(1+max)

        for i in range(len(self.a)):
            element = self.a[i]
            self.k[element] = self.k[element]+1

        for i in range(len(self.a)):
           self.a[i] = self.a[i]-min

    def search(self, val):
        min = 0
        max = 0

        for i in self.a:
            if i > max:
                max = i
            elif i < min:
                min = i

        if min < 0:
            min = min * (-1)

        val = val+min

        if self.k[val] != 0:
            return True
        else:
            return False

    def sort(self):
        min = 0
        max = 0
        s = [0]*len(self.a)
        index = 0

        for i in self.a:
            if i > max:
                max = i
            elif i < min:
                min = i

        if min < 0:
            min = min * (-1)

        for i in range(len(self.k)):
            if self.k[i] != 0:
                for j in range(self.k[i]):
                    s[index] = i-min
                    index += 1

        for i in range(len(s)):
            self.a[i] = s[i]

        return self.a


arr = [9,-3,-4,5,-3]

b = KeyIndex(arr)
print(b.search(3))
print(b.sort())