#Aditi Saha Ria
#ID: 20101238
#Task_06


def binary_search(arr, l, r, val):
    if l <= r:
        m = (l+r)//2

        if val == arr[m]:
            return m
        elif val>arr[m]:
            return binary_search(arr, m+1, r, val)
        else:
            return binary_search(arr, l, m-1, val)
    return -1

arr = [10,20,30,40,50,60]
value = 40

ans = binary_search(arr, 0, len(arr)-1, value)

if ans == -1:
    print('Value not found')
else:
    print(f'Value is present at index no {ans}')
