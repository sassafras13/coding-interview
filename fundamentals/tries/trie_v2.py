# 01 - 12 - 2021
# Emma Benjaminson
# Implementation v2 of a Trie
# Source: https://albertauyeung.github.io/2020/06/15/python-trie.html

class TrieNode: 
    """
    A node in the trie structure.
    """

    def __init__(self, char):

        # the character stored in this node
        self.char = char

        # if this can be the end of a word
        self.is_end = False

        # a counter indicating how many times a word is inserted
        # (only if this node's is_end is True)
        self.counter = 0

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}

class Trie(object):
    """
    The trie object.
    """

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any characters.
        """

        self.root = TrieNode("")

    def insert(self, word):
        """
        Insert a word into the trie.
        """

        node = self.root

        # loop through each character in the word
        # check: if there is no child containing the character
        # then create a new child for the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # if a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        # mark the end of a word
        node.is_end = True

        # increment the counter to indicate that we see this word again
        node.counter += 1

    def dfs(self, node, prefix):
        """
        Depth-first traversal of the trie.
        
        Args: 
            - node: the node to start with
            - prefix: the current prefix, for tracing a word while traversing the trie
        """

        if node.is_end:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x):
        """
        Given an input (a prefix), retrieve all words stored in the trie with that prefix, sort hte words by the number of times they have been inserted.
        """

        # use a variable within the class to keep all possible outputs
        # as there can be more than one word with such prefix
        self.output = []
        node = self.root

        # check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot find the prefix, return empty list
                return []

        # traverse the trie to get all candidates
        self.dfs(node, x[:-1]) # gets all the elements from x except the last element

        # sort the results in reverse order and return
        # sorted is a function for sorting a list
        # sorted(iterable, key=key, reverse=reverse)
        # lambda is a small anonymous function with input argument x
        # reverse = True means sort descending
        return sorted(self.output, key=lambda x: x[1], reverse=True)
