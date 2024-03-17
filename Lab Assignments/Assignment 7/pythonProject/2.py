#Aditi Saha Ria
#ID: 20101238
#Task 01

class Hashing:
    def __init__(self, arr):
        self.arr = arr

    def hash_calculation(self):

        str_list = [0]*len(self.arr)

        for j in self.arr:
            sum = 0
            const = 0
            for i in j:
                if (ord(i) > 65 and ord(i) < 69) or (ord(i) > 69 and ord(i) < 73) or (ord(i) > 73 and ord(i) < 79) or (
                        ord(i) > 79 and ord(i) < 85) or (ord(i) > 85 and ord(i) < 91):
                    const += 1

                elif ord(i) > 47 and ord(i) < 58:
                    sum = sum + int(i)

            index = ((const * 24) + sum) % 9

            if str_list[index]==0:
                str_list[index] = j
            else:
                for k in range(index+1,len(str_list)):
                    if str_list[k] == 0:
                        str_list[k] = j
                        break
                else:
                    for l in range(index):
                        if str_list[l] == 0:
                            str_list[l] = j
                            break

        return str_list

a = ['ST189B832','ST189B832','ABCU123','AB123','ABX']
b = Hashing(a)
print(b.hash_calculation())
