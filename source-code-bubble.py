def bubbleSort(arr):
    for step in range(0, len(arr)):
        for i in range(0, len(arr)-step-1):
            if(arr[i] > arr[i+1]):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr

mylist = [5, 4, 10, 8, 23, 42, 1, 22]
mylist = bubbleSort(mylist)
print(mylist)

