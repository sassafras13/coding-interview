# 2021-05-20
# Emma Benjaminson
# Queue Implementation

# for Ch04 - P01 at least

class Queue(object):
    
    # initialize the queue as a list
    def __init__(self):

        self.queue = []

    # enqueue method adds an element to the front of the list (via insert)
    def enqueue(self, val):
        self.queue.insert(0, val)

    # dequeue method pops an element from the back of the list
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    # is_empty method checks if the list is empty
    def is_empty(self):
        return len(self.queue) == 0
