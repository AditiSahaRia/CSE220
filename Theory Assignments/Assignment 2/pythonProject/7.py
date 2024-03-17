def count(arr1, arr2):
    for i in arr2:
        count = 0
        for j in arr1:
            if i>=j:
                count += 1
            else:
                break
        print(count, end=' ')

a = input()
b = input()
c = input()
Arr1 = [0]*int(a[0])
Arr2 = [0]*int(a[-1])
counter = 0
for i in b:
    if i != ' ':
        Arr1[counter] = int(i)
        counter += 1
counter = 0
for i in c:
    if i != ' ':
        Arr2[counter] = int(i)
        counter += 1
count(Arr1, Arr2)