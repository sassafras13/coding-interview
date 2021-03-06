# 2021-02-01
# Emma Benjaminson
# Chapter 1 Problem 1.1 Is Unique

# Problem: implement an algorithm to determine if a string has all unique characters. 

# Emma thinking out loud: 
# the naive approach is just to have a list of all the chars in the string
# as you run through the string, check to see if the char exists in the list, and if not, add it
# if the char does exist, stop the loop and report that there's a duplicate

# Emma's questions:
# can I just store chars in a list in Python? 
# what is the runtime of running through a string? 
# what is the runtime of searching through a list for a char? 
# should the list be alphabetical or just a queue/stack?

# MODIFICATION: 
# what if you cannot use additional data structures? 

# Emma thinking out loud: 
# so now I can't use a list structure in Python? 
# I guess for every char in the string, I need to continue searching through the string to see if I can find a duplicate



def isUnique(string):

    # create empty list to store characters
    char_list = []

    # iterate through chars in the string
    for char in string:

        # check if char is in char_list
        if char in char_list:

            # end the loop
            isUnique = False
            return isUnique

        else:
            char_list.append(char)

    isUnique = True
    return isUnique

def isUniqueMod(string):

    # create a counter of where we are in the string
    counter = 0

    # iterate through the chars in the string
    for char in string: 

        # increment the counter
        counter += 1

        # run through the rest of the string
        for check_char in string[counter:]:
            
            # if the char matches with a char further along in the string
            # then we have a duplicate
            if char == check_char:
                #print("char is ", char)
                #print("check_char is ", check_char)
                return False

            # otherwise we keep running and exit the inner loop

    # if we make it this far than we never found a duplicate
    return True

# driver code
if __name__ == "__main__":

    # test 1
    str1  = "hello"
    print("Test string 1: ", str1)
    print(isUnique(str1))

    # test 2
    str2 = "align"
    print("Test string 2: ", str2)
    print(isUnique(str2))

    # test 3 
    str3 = "she rules"
    print("Test string 3: ", str3)
    print(isUnique(str3))

    # MOD test 1
    print("Mod test string 1: ", str1)
    print(isUniqueMod(str1))

    # MOD test 2
    print("Mod test string 2: ", str2)
    print(isUniqueMod(str2))

    # MOD test 3
    print("Mod test string 3: ", str3)
    print(isUniqueMod(str3))
