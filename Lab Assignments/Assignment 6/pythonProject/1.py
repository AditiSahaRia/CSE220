#Aditi Saha Ria
#ID: 20101238
#Task_01

def selection_sort(a,i,j):
    l = len(a)
    if i == l and j == l:
        return -1
    if i < l - 1:
        min = i
        while j < l:
            if a[j] < a[min]:
                min = j
            j = j + 1
        if min != i:
            temp = a[i]

            a[i] = a[min]

            a[min] = temp
        selection_sort(a, i + 1, i + 2)

A=[13,25,0,-4,7,-1,18,9,-6,21]

i=0

j=i+1

selection_sort(A,i,j)

print(A)