# 2021-01-26
# Emma Benjaminson
# Binary Search Implementation
# Source: https://realpython.com/binary-search-python/

# iterative implementation
def find_index(elements, value):
    left, right = 0, len(elements) - 1
    middle = (left + right) // 2

    while left <= right: 
        if elements[middle] == value:
            return middle

        if elements[middle] < value:
            left = middle + 1
        elif elements[middle] > value: 
            right = middle - 1

# implementation for searching iteratively by key
def find_index_key(elements, value, key):
    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_element = key(elements[middle]) # the key is a function you can run on elements[middle]

        if middle_element == value:
            return middle

        if middle_element < value: 
            left = middle + 1
        elif middle_element > value:
            right = middle - 1

# driver code
fruits = ['orange', 'plum', 'watermelon', 'apple']
print(fruits.sort(key=len))

print(fruits[find_index_key(fruits, key=len, value=10)])

print(find_index_key(fruits, key=len, value=3))