# Source: https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/chapter_01/p01_is_unique.py
# See this post about unicode vs ascii: https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/

# O(N)
import unittest # a testing framework module


def is_unique_chars_algorithmic(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    # this is a pythonic and faster way to initialize an array with a fixed value.
    #  careful though it won't work for a doubly nested array
    # this is a hashed approach because ord() does the hashing (I think?)
    char_set = [False] * 128
    for char in string:
        val = ord(char) # ord converts the char to the Unicode equivalent
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True


def is_unique_chars_pythonic(string):
    return len(set(string)) == len(string) # set creates a set from all the chars in string


def is_unique_bit_vector(string):
    """Uses bitwise operation instead of extra data structures."""
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    checker = 0
    for c in string:
        val = ord(c)
        if (checker & (1 << val)) > 0: # << shifts 1 over to the left [val] number of bits
            return False
        checker |= 1 << val # union of checker and 1 << val
    return True

# this class is a subclass of the TestCase of the unittest module
class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]
    test_functions = [
        is_unique_chars_pythonic,
        is_unique_chars_algorithmic,
        is_unique_bit_vector,
    ]

    # name all the tests with names starting with "test_"
    # this function actually iterates through specific functions to be tested
    def test_is_unique_chars(self):
        for is_unique_chars in self.test_functions:
            for text, expected in self.test_cases:
                assert is_unique_chars(text) == expected


if __name__ == "__main__":
    unittest.main()
