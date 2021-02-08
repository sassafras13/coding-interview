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
        # then we swap that element with its neighbor and move the 
        # partition frontier over? 
        if arr[i] <= arr[0]:
            
            # current_position only increments if we found an element
            # that needs to move to the other side of the partition
            current_position += 1

            # save the value of the i-th element in temp
            temp = arr[i] 
            
            # swap the current position element into the i-th element
            arr[i] = arr[current_position] 

            # assign the i-th element (that is smaller than partition)
            # to the current position value in the array
            arr[current_position] = temp

    # these steps move the partition element to its correct location 
    # in the array
    temp = arr[0]
    arr[0] = arr[current_position]
    arr[current_position] = temp

    # now sort elements to the left and right of the partition 
    left = QuickSort(arr[0:current_position])
    right = QuickSort(arr[current_position+1:elements])

    # merge everything together
    arr = left + [arr[current_position]] + right

    return arr

array_to_sort = [4, 2, 7, 3, 1, 6]
print("original array: ", array_to_sort)
print("sorted array: ",QuickSort(array_to_sort))
