# source: https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/chapter_03/p01_three_in_one.py

# Their solution appears to be similar to mine
# use a list to store three stacks
# use a second list to keep track of the sizes of each stack
# the push and pop methods are standard, there are no surprises in how they work
# compared to a normal stack

# I actually don't get how this implementation addresses some of the hints given in the book?
# like what about the circular nature of the indexing? 
# or the fact that we could cleverly allocate space to different size stacks?

class MultiStack:

    def __init__(self, stack_size, number_of_stacks):
        self.number_of_stacks = number_of_stacks
        self.array = [0] * (stack_size * self.number_of_stacks)
        self.sizes = [0] * self.number_of_stacks
        self.stack_size = stack_size

    def push(self, value, stack_num):
        self._assert_valid_stack_num(stack_num) # clever to include a check on stack_num
        if self.is_full(stack_num):
            raise StackFullError(f"Push failed: stack #{stack_num} is full")
            # check that stack is not full
        self.sizes[stack_num] += 1 # increment the size of the stack that was pushed to
        self.array[self.index_of_top(stack_num)] = value # add the value to the stack

    def pop(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        if self.is_empty(stack_num):
            raise StackEmptyError(f"Cannot pop from empty stack #{stack_num}")
            # these custom errors are classes that inherit from the Exception class
            # or the ValueError class
        value = self.array[self.index_of_top(stack_num)]
        self.array[self.index_of_top(stack_num)] = 0
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        if self.is_empty(stack_num):
            raise StackEmptyError(f"Cannot peek at empty stack #{stack_num}")

        return self.array[self.index_of_top(stack_num)]

    def is_empty(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        return self.sizes[stack_num] == self.stack_size

    def index_of_top(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1

    def _assert_valid_stack_num(self, stack_num):
        if stack_num >= self.number_of_stacks:
            raise StackDoesNotExistError(f"Stack #{stack_num} does not exist")

class MultiStackError(Exception):
    """multistack operation error"""


class StackFullError(MultiStackError):
    """the stack is full"""


class StackEmptyError(MultiStackError):
    """the stack is empty"""


class StackDoesNotExistError(ValueError):
    """stack does not exist"""
