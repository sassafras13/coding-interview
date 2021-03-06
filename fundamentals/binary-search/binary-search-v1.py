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

# recursive implementation
def contains(elements, value):
    left, right = 0, len(elements) - 1

    if left <= right:
        middle = (left + right) // 2

        if elements[middle] == value:
            return True

        if elements[middle] < value: 
            return contains(elements[middle + 1:], value) 
        elif elements[middle] > value: 
            return contains(elements[:middle], value)

    return False

# driver code

fruits = ['orange', 'plum', 'watermelon', 'apple']
print(fruits)
fruits.sort(key=len) # sorts the list in ascending order by the length of the word
print(fruits)

print(fruits[find_index_key(fruits, key=len, value=10)])

print(find_index_key(fruits, key=len, value=3))

myList = [1, 3, 65, 135, 342]
print(contains(myList, value=342))
