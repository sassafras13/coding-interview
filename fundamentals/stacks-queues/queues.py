# 2021-01-20
# Emma Benjaminson
# Implementation of queues
# Source: https://medium.com/@kojinoshiba/data-structures-in-python-series-2-stacks-queues-8e2a1703d67b

class Queue: 
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.insert(0,val)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

if __name__ == "__main__":

    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("what is the size of the queue?")
    print(queue.size())

    print("dequeue the first element")
    print(queue.dequeue())

    print("what is the size now?")
    print(queue.size())

    print("is the queue empty?")
    print(queue.is_empty())
