# 2021-05-14
# Emma Benjaminson
# Chapter 3 Problem 1: Stacks and Queues

# Problem: Describe how you could use a single array to implement three stacks. 

# Emma thinking out loud:
# so a 1D array can be used to build a single stack by push/pop operations on the end of the array
# if we had a 3 x n 2D array, then each row of the array could correspond to a different stack 
# the calls to each stack should clarify which stack we are talking about and this can be converted to 
# a row in the array accordingly

# I read hints 2 and 12
# one thing I forgot is if each stack is a different size we'll still need all of the rows to be
# as long as the longest stack
# also we could keep to a 1D array and just allocate different lengths within that array to each stack

# hints 38 and 58
# can shift stacks around to use up all the available space
# think of the array as circular, i.e. the end wraps back around to the beginning...

# ...okay...
# so I think multiple rows is not part of the solution. I think when they say array they mean list, not a numpy array
# if I had evenly allocated space on the list to each stack, then what order they were in wouldn't matter
# unless traversing the list takes time, in which case I would want to put the longest? shortest? stack first?
# example: 
# [abcde---][abc-----][a-------]
# so if my longest stack has more stuff added, then I need to extend all 3 segments? 
# [---edcba][-----cba][-------a]
# [abcde][abc][a][---------------]

# could I just keep track of the index for the end of each stack in the list
# then I just have to go to that index, shift everything else forwards and add in an extra element there?
# that's kind of expensive

# what about this: 
# [a][abc][abcde][---------------]

# now I only have to do that if I need to move the shorter lists around
# the problem with this arrangement is that I'm going to have to move stuff around a lot
# with the first configuration, I can push/pop 3-7 elements per stack before I need to reallocate space

# I care about using all available space because creating a new, larger list is time/memory expensive
# how can I be flexible about moving stuff within the list? 
# maybe its where I put the partitions between stacks? 

# [abcde---][-----cba][a-------]

# now I can move the partition between stack 1 and 2 as necessary
# still not getting the circular hint...
# let's try something, let's try this idea above

# -------------------------------------------------------------------------------------------------

import unittest

# create stack3 class
class stackThree:

    # a list with pre-allocated size (multiple of 3) 
    # size is n
    def __init__(self, n):
        # thanks https://stackoverflow.com/questions/521674/initializing-a-list-to-a-known-number-of-elements-in-python
        self.stacks = [None for x in range(3*n)]
        self.idx = [0, ((2*n)-1), (2*n)]  

    # end of stack 1 is located at index 0
    # end of stack 2 is located at index 2n-1
    # end of stack 3 is located at index 2n

    # stacks 1 and 3 grow left -> right
    # stack 2 grows right -> left

    # push method
    def push(self, nStack, x):

        # find the index of the end of the nStack stack
        index = self.idx[nStack-1]
       
        # the position at this index should be empty, so replace the element here with x
        self.stacks[index] = x

        # update the index to be +1 if nStack == 1 | 3 else -1
        if nStack == 1 or 3:
            self.idx[nStack-1] += 1
        else: 
            self.idx[nStack-1] -= 1

        # return the list and the indices
        return self.stacks, self.idx

    # pop method
    def pop(self, nStack):

        # find the index of the end of the nStack stack
        index = self.idx[nStack-1]

        # the element at the index before this value should be the last element
        # copy this final element to a new variable
        popVal = self.stacks[index-1]

        # then set this new variable to None
        self.stacks[index-1] = None

        # update the index to be -1 if nStack == 1 | 3 else +1
        if nStack == 1 or 3:
            self.idx[nStack-1] -= 1
        else:
            self.idx[nStack-1] += 1

        # return the popped value, the list and the indices
        return popVal, self.stacks, self.idx

    # peek method
    def peek(self, nStack):

        # do the same thing as pop() method without deleting the variable 
        # find the index of the end of the nStack stack
        index = self.idx[nStack-1]

        # the element at the index before this value should be the last element
        # copy this final element to a new variable
        peekVal = self.stacks[index-1]

        # return the peek value
        return peekVal

    # isEmpty method
    def isEmpty(self):
        
        # use isEmpty variable to answer this question
        isEmpty = True

        # iterate through the list
        for i in range(len(self.stacks)):

            if self.stacks[i] is not None:
                isEmpty = False
                break
            
        # if one of the elements is not None then break the loop
        # return isEmpty = False
        return isEmpty


# for testing
#class Test(unittest.TestCase):
    
#    test_cases = [
#            (



#if __name__ == "__main__":


