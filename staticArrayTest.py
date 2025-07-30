from staticArray import removeEnd, insertEnd, insertMiddle, removeMiddle, printArr

arr = [1, 2, 3, 4, 0, 0]
#printArr(arr, 6)
print(arr)
length = removeEnd(arr, 4)
print(arr)
print(length)

insertEnd(arr, 5, length, 6)
length = insertMiddle(arr, 2, 99, length)
print(arr)
print(length)

length = removeMiddle(arr, 2, length)
print(arr)
print(length)

printArr(arr, 6)