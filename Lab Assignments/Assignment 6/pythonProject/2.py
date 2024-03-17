#Aditi Saha Ria
#ID: 20101238
#Task_02

def insertion_sort(a,i):
    l = len(a)

    if i == l:
        return -1

    if i < l:

        j = i - 1

        key = a[i]

        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]

            j = j - 1

        a[j + 1] = key

        insertion_sort(a, i + 1)

b=[22,5,14,2,7,1]

i=1

insertion_sort(b,i)

print(b)