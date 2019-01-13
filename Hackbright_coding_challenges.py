import math
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
    >>> lemur([0, 0, 1, 1, 0, 0])
    3
    """

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    jumps = 0
    i = 0

    # if list is empty or 1, exit with jumps at 0
    if len(branches) <= 1:
        return 0

    elif len(branches) == 2:
        return 1

    while i < (len(branches) - 2):
        # check if the next item and the item after that are 0
        # if so, jump 2 branches at once.
        if (branches[i + 1] == 0 and branches[i + 2] == 0) or branches[i + 1] == 1:
            jumps += 1
            i += 2

        elif branches[i + 1] == 0:
            jumps += 1
            i += 1

    return jumps

######### Missing Number
# Imagine a list of numbers from 1 to max_num, inclusive – except that 
# one of these numbers will be missing from the list.

# You should write a function that takes this list of numbers, 
# as well as the max_num, and it should return the missing number.

# For example, given a list of numbers, in random order, of 1..10, 8 
# was removed. Your function would be given the list and the max_num (10), 
# and it should find 8:

def missing_number(lst, max_num):
    """
    A function that takes this list of numbers, 
    as well as the max_num, and it should return the missing number.

    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8

    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8
    """

    # Step 1 (easiest)
    # Initially, focus on reducing runtime—this should be solvable in O(n) time. 
    # You can create an additional list/set/dictionary if necessary.

    num_set = set(lst)

    for i in range(1, max_num + 1):
        if i not in num_set:
            return i

# Step 2 (harder)
# Now, think about reducing memory use—did your first solution require you to keep 
# a new list/set/dictionary? Can you think of a different way to think about the 
# problem that doesn’t use additional memory, even if it takes more time?

# There’s a way you could solve this in O(n log n) time that doesn’t 
# require creating another large data structure (technically, while being 
# O(n log n) in runtime, it is O(1) in “runspace”—it uses the same amount 
# of memory no matter how big n is)

# 



#Given an word and a dictionary. Find all anagrams of the word in the dictionary
word = "madam"
dictionary = ["set", "this", "aadmm", "oolrs"]

def hash_word(word):
    dict_out = {}
    for letter in word:
    #     if letter in dict_out:
    #         dict_out[letter] += 1
    #     else:
    #         dict_out[letter] = 0
        dict_out[letter] = dict_out.get(letter, 0) + 1
    return dict_out

def is_anagram(word1, word2):

    if len(word1) != len(word2):
        return False

    d1 = hash_word(word1)
    d2 = hash_word(word2)
    
    if len(d1) != len(d2):
        return False

    for key in d1.keys():
        if key not in d2:
            return False
        if d1[key] != d2[key]:
            return False

    return True

def check_for_anagrams_in_list(ref_word, word_list):
    anagram_list = []
    for word in word_list:
        if is_anagram(ref_word, word):
            anagram_list.apend(word)
    return anagram_list


####### Given a DNA strand, return it's compliment

def get_dna_compliment(dna):
    """ (str) -> str
    Given a DNA strand(dna) as a string, return it's compliment

    >>> get_dna_compliment('AAACGT')
    'TTTGCA'
    >>> get_dna_compliment('CGCGCG')
    'GCGCGC'
    """
    # create a new string that starts empty
    # loop over each letter in the string
    # use conditional logic to add compliment 
    # to new string
    dna = dna.upper()
    dna_compliment = ''

    for letter in dna:
        if letter == 'A':
            dna_compliment += 'T'
        elif letter == 'T':
            dna_compliment += 'A'
        elif letter == 'C':
            dna_compliment += 'G'
        else:
            dna_compliment += 'C'

    return dna_compliment


############### Given a string, find the largest word that has even length
def find_max_even_word(string):
    """
    Given a string, find the largest word that has even length.

    >>> find_max_even_word("Tis the hardest things")
    'things'
    """

    s_lst = string.split()
    max_even_word = ""
    for word in s_lst:
        if len(word) % 2 == 0:
            if len(word) > len(max_even_word):
                max_even_word = word
    return max_even_word



############ Given a string split into segments for texting
# Each message is <= 160 characters
# A suffix is attached to each segmented text Ex: (1/1)
# A suffix is therefore 5 characters long
# Due to suffix length, segmented messages can only be 155 characters long
# A message < 160 characters does not need a suffix
# If a segmented message starts with a space, that space is removed - KEY POINT

# Ex: "This is a string that needs to be segmented."
# This is a (1/3) # space is not built in, but is the last character before the break
# string that needs (2/3) # space is removed before each line (rstrip?)
# to be segmented.(3/3) # space removed before each line

### Test case using numbers to solidify thoughts
# Ex: "012 4567 91011" # Message length of 4
# 012 (suffix)
# 4567(suffix)
# 9101(suffix) # space stripped off front
# 1(suffix)

def segment_message(message):
    """
    >>> segment_message("012 4567 91011")
    ['012 (1/4)', '4567(2/4)', '9101(3/4)', '1(4/4)']
    """
    # First check if the message is < 160 characters
    if len(message) <= 4:
        return message

    MAX_CHAR = 4

    # keep track of the starting and ending points
    start = 0  #4  8   12
    end =   4  #8  12  16

    segment_counter = 1  

    string_array = []
    num_segments = math.ceil(len(message) / MAX_CHAR)

    while start < len(message):
        if message[start] == " ":
            start += 1
            end += 1

        segment = message[start:end]
    
        start += MAX_CHAR
        end += MAX_CHAR
        suffix = f"({segment_counter}/{num_segments})"
        string_array.append(f"{segment}{suffix}")

        segment_counter += 1

    return string_array


if __name__ == "__main__":
    import doctest
    
    result = doctest.testmod()
    if result.failed == 0:
        print("ALL TESTS PASSED")



