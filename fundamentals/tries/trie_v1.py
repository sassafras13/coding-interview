# 01-11-2021
# Emma Benjaminson  
# Trie Implementation
# Source:  https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1

# a tuple is a built-in data type in Python that stores data 
# ordered and unchangeable
# written with round brackets
from typing import Tuple

# object is an identifier that refers to a builtin type
class TrieNode(object):
    """
    Basic trie node implementation.
    """

    def __init__(self, char: str):
       self.char = char
       self.children = []

       # check if it is the last char in word
       self.word_finished = False

       # how many times has this char appeared
       self.counter = 1

def add(root, word: str):
    """
    Adding a word in the trie structure
    """
    
    node = root
    for char in word:
        found_in_child = False

        # search for the char in the children of the current node
        for child in node.children:
            if child.char == char:

                # we found the char, increase counter by 1 to record that another word shares this char
                child.counter += 1

                # point the node to the child that contains this char
                node = child

                found_in_child = True
                break

        # otherwise we did not find the char so we add a new child node
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)

            # then point the node to the new child
            node = new_node

    # finished running through the word
    node.word_finished = True

# the syntax "prefix: str" means that the input, prefix, must be type string
# similarly the syntax "-> Tuple[bool, int]" means that the output must be type Tuple
def find_prefix(root, prefix: str) -> Tuple[bool, int]:
    """
    Check and return:
        1. If the prefix exists in any of the words we have already added
        2. If yes then how many words have the prefix
    """

    node = root

    # if the root node has no children, then return False
    # because this means we are trying to search an empty trie
    if not root.children:
        return False, 0

    for char in prefix:
        char_not_found = True

        # search through all the children of the present node
        for child in node.children:
            if child.char == char:
                
                # we found the char among the children
                char_not_found = False

                # assign node as the child containing the char
                node = child
                break

        # return false when we do not find the char
        if char_not_found:
            return False, 0

    # if we are still in the function at this line then we have found the prefix
    # we return the counter to indicate how many words have this prefix
    return True, node.counter

if __name__ == "__main__":
    root = TrieNode('*')
    add(root, "hackathon")
    add(root, "hack")

    print(find_prefix(root, "hac"))
    print(find_prefix(root, "hack"))
    print(find_prefix(root, "hackathon"))
    print(find_prefix(root, "ha"))
    print(find_prefix(root, "hammer"))
