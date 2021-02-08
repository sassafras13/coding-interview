# 2021-01-30
# Emma Benjaminson
# Implementation of Mergesort
# Source: https://www.geeksforgeeks.org/merge-sort/

def mergeSort(arr):

    if len(arr) > 1:

        # find the middle of the array
        mid = len(arr) // 2

        # divide up the array elements into two halves
        L = arr[:mid]
        R = arr[mid:]

        # sort each half
        mergeSort(L)
        mergeSort(R)

        # create indices for copy process
        i = j = k = 0

        # copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            # if this item of L is less than R then
            # we make it the k-th element of arr
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            # otherwise if R is less than L then 
            # we make that the k-the element of arr
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # check if any elements were left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# code for printing the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# driver code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is ", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
