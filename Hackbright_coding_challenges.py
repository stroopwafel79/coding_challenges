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



if __name__ == "__main__":
    import doctest
    
    result = doctest.testmod()
    if result.failed == 0:
        print("ALL TESTS PASSED")



