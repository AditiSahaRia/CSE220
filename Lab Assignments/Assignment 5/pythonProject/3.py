def array_elemnents(arr):
    if len(arr)>1:
        a = arr[0]
    else:
        return arr[0]
    arr = arr[1:]
    return f'{a}, {array_elemnents(arr)}'
lst = [1,3,4,5,6,7,2]
print(array_elemnents(lst))