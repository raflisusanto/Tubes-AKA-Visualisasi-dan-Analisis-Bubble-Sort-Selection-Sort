def selectionSort(arr):
    for Pass in range(1, len(arr)):
        idx = Pass - 1
        for i in range(Pass, len(arr)):
            if arr[idx] > arr[i]:
                idx = i
        temp = arr[Pass-1]
        arr[Pass-1] = arr[idx]
        arr[idx] = temp
    return arr

mylist = [5, 4, 10, 8, 23, 42, 1, 22]
mylist = selectionSort(mylist)
print(mylist)



