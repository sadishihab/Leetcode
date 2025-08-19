#Testing the static array

from static_array import removeEnd, insertEnd, insertMiddle, removeMiddle, printArr

arr = [1, 2, 3, 4, 0, 0]
print("Original array\n", arr)

length = insertEnd(arr, 5, 4, 6)
print("Inserting 5 at the end\n", arr)
print("Current length of non-zero elements", length)

length = removeEnd(arr, length)
print("Removing the last non-zero element\n", arr)
print("Current length of non-zero elements", length)

length = insertMiddle(arr, 2, 99, length)
print("Inserting 99 in second index\n", arr)
print("Current length of non-zero elements", length)

length = removeMiddle(arr, 2, length)
print("Remove element from the secod index\n", arr)
print("Current length of non-zero elements", length)

printArr(arr, 6)