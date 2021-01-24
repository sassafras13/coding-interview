# 01-07-2021
# Emma Benjaminson  
# Hash Table Implementation
# Source: https://stephenagrice.medium.com/how-to-implement-a-hash-table-in-python-1eb6c55019fd

INITIAL_CAPACITY = 50

class HashTable:
    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity
 
    def hash(self, key):
        hashsum = 0
        
        # for each char in the key
        for idx, c in enumerate(key):
            # add (index + length of key) ^ (current char code)
            hashsum += (idx + len(key)) ** ord(c)

            # modulus to keep hashsum in range [0, self.capacity-1]
            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value):

        # 1 - increment size
        self.size += 1

        # 2 - compute index of key
        index = self.hash(key)

        # go to the node corresponding to the index
        node = self.buckets[index]

        # 3 - if bucket is empty, create node 
        if node is None:
            self.buckets[index] = Node(key, value)
            return

        # 4 - if there is a collision, iterate to the end of the linked list at this index 
        # and add a new node 
        prev = node
        while node is not None:
            prev = node
            node = node.next

        prev.next = Node(key, value)

    def find(self, key):

        # 1 - compute hash
        index = self.hash(key)

        # 2 - go to first node in list at this index
        node = self.buckets[index]

        # 3 - traverse linked list at this node
        while node is not None and node.key != key:
            node = node.next

        # 4 - now node is the requested key/value pair or None
        if node is None:
            return None
        else:
            return node.value

    def remove(self, key):
        # 1 - compute hash
        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        # 2 - iterate to the requested node
        while node is not None and node.key != key:
            prev = node
            node = node.next

        # 3 - now node is either the requested node or None
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            
            # delete this element from linked list
            if prev is None: 
                node = None
            else:
                prev.next = prev.next.next
            return result

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


