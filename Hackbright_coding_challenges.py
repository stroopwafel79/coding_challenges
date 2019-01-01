#############Is the word an anagram of a palindrome?
# A palindrome is a word that reads the same forward and backwards 
# (eg, “racecar”, “tacocat”). An anagram is a rescrambling of a word (eg for “racecar”, you could rescramble this as “arceace”).
# Determine if the given word is a re-scrambling of a palindrome.
# The word will only contain lowercase letters, a-z.

def make_dict(s):
    
    letter_dict = {}
    for letter in s:
        letter_dict[letter] = letter_dict.get(letter, 0) + 1

    return letter_dict


def is_anagram_of_palindrome(s):
    """ Take in a string and determine if it is an anagram of a palindrome.

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False
    """

    # Only one letter is allowed to be odd.
        
    d = make_dict(s)
    
    num_odd = 0
    
    for value in d.values():
        if value % 2 != 0:
            num_odd +=1
    
    if num_odd > 1:
        return False
    
    return True

#########Count List Recursively

def count_recursively(lst):
    """Return number of items in a list, using recursion.

    >>> count_recursively([])
    0

    >>> count_recursively([1, 2, 3])
    3
    """

    if lst == []:
        return 0
    
    lst.pop()
    return count_recursively(lst) + 1


#########Binary Search

def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses.
    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    >>> max([binary_search(i) for i in range(1, 101)])
    7
    """
    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 0

    too_low = 0
    too_high = 101
    guess = None

    while val != guess:
        guess = int((too_high - too_low) / 2) + too_low
        num_guesses += 1


        if guess > val:
            too_high = guess

        if guess < val:
            too_low = guess
        
    return num_guesses

#########Decode a string

# In this challenge, you’ll write a decoder.

# A valid code is a sequence of numbers and letters, always starting with a number 
# and ending with letter(s).

# Each number tells you how many characters to skip before finding a good letter. 
#After each good letter should come the next next number.

# For example, the string “hey” could be encoded by “0h1ae2bcy”. This means “skip 0, 
#find the ‘h’, skip 1, find the ‘e’, skip 2, find the ‘y’”.

# A single letter should work:

def decode(s):
    """Decode a string(s). A valid code is a sequence of numbers and letters, 
       always starting with a number and ending with letter(s).
       Each number tells you how many characters to skip before finding a 
       good letter. After each good letter should come the next next number.

    >>> decode("0h")
    'h'
    >>> decode("2abh")
    'h'
    >>> decode("0h1ae2bcy")
    'hey'
    """
    # Loop through string via indexs.
    # First check if value @ index is a number.
    # If so, skip that many places.
    # Add index at number + number to get index of letter.
    new_string = ""

    for i in range(len(s)):
        if s[i].isdigit():
            # print("s[i]", s[i])
            # print("s[int(s[i]) + 1]", s[int(s[i]) + 1])
            new_string += s[int(s[i]) + i + 1]
            #print("new_string:", new_string)

    return new_string


#######Leaping Lemur

# A lemur wants to jump across a span in the forest on branches. She can 
# jump 1 or 2 branches at a time. Unfortunately, some of the branches 
# are on dead trees, and she can’t use those branches to jump.

# For example:
# The black circles are dead branches. In this example, the lemur starts on 
# the first branch, and jumps 1 to branch #2 (she can’t jump 2 to 
# branch #3, as it’s dead). She then jumps from 2 to 4 and from 4 to 6. 
# As she ends up on the last branch, she’s finished.
# The first and last branch will always be alive, and there will 
# never be two dead branches in a row (that is, it will always be 
# possible for her to make this trip).
# Your challenge is to calculate how many jumps she needs to make.

# Code
# You’ll be given a list of the branches, like:

# [0, 0, 1, 0, 1, 0]
# 0 represents alive branches and 1 represents dead branches. The lemur starts on the first branch in the list (index 0) and is finished when she reaches the last branch in the list.

# Write a function that returns the number of jumps needed:

def  lemur(branches):
    """Return number of jumps needed.
    >>> lemur([0])
    0
    >>> lemur([0, 0])
    1
    >>> lemur([0, 0, 0])
    1
    >>> lemur([0, 1, 0])
    1
    >>> lemur([0, 0, 1, 0])
    2
    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5
    """

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"


if __name__ == "__main__":
    import doctest
    
    result = doctest.testmod()
    if result.failed == 0:
        print("ALL TESTS PASSED")



