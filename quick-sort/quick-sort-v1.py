# 2021-01-30
# Emma Benjaminson
# Quick Sort Implementation
# Source: https://www.educative.io/edpresso/how-to-implement-quicksort-in-python

def QuickSort(arr):

    elements = len(arr)

    # base case
    if elements < 2:
        return arr

    current_position = 0 # position of the partitioning element

    # partitioning loop
    for i in range(1, elements):
        # if the i-th element is smaller than the partitioning element
        # then we ???
        if arr[i] <= arr[0]:
            current_position += 1
            temp = arr[i] # save the value of arr[i] in temp
            arr[i] = arr[current_position]
