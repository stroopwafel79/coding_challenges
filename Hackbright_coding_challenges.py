import math
from random import sample

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
        
    return num_odd < 2

######### Count List Recursively ############

def count_recursively(lst):
    """Return number of items in a list, using recursion.

    >>> count_recursively([])
    0

    >>> count_recursively([1, 2, 3])
    3
    """

    if not lst:
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
        guess = (too_high - too_low) // 2 + too_low
        num_guesses += 1


        if guess > val:
            too_high = guess

        if guess < val:
            too_low = guess
        
    return num_guesses

######### Decode a string ########

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
            new_string += s[int(s[i]) + i + 1]

    return new_string


####### Leaping Lemur #######

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

## HB Solution ##
# def  lemur(branches):
#     """Return number of jumps needed."""

#     assert branches[0] == 0, "First branch must be alive"
#     assert branches[-1] == 0, "Last branch must be alive"

#     # START SOLUTION

#     at = 0
#     n_jumps = 0

#     while at < len(branches) - 1:
#         at += 2
#         if at >= len(branches) or branches[at] == 1:
#             # We can jump this far, so only jump 1
#             at -= 1
#         n_jumps += 1

#     return n_jumps

######### Missing Number #########
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

    # lst.sort() # sorts list in place so no additional memory used.
    # i = 0

    # while i < (len(lst)):
    #     if lst[i] != i + 1:
    #         return i + 1

    #     i += 1



########### Hacker Rank Problem - Anagrams in List ############
#Given an word and a list. Find all anagrams of the word in the dictionary

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

    # word lengths must be the same to be an anagram
    if len(word1) != len(word2):
        return False

    # make a letter frequency dictionary of each word
    d1 = hash_word(word1)
    d2 = hash_word(word2)

    return d1 == d2


def check_for_anagrams_in_list(ref_word, word_list):
    """ Return list of words from word_list that are anagrams of ref_word
    >>> check_for_anagrams_in_list("madam", ["set", "this", "aadmm", "oolrs"])
    ['aadmm']
    >>> check_for_anagrams_in_list("to", ["set", "ot", "too", "to"])
    ['ot', 'to']
    """
    anagram_list = []
    for word in word_list:
        #print(is_anagram(ref_word, word))
        if is_anagram(ref_word, word):

            anagram_list.append(word)
    return anagram_list


####### Given a DNA strand, return it's compliment ##########

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
    # Use dictionary of compliment values 
    dna = dna.upper()
    dna_compliment = ''
    compliment = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 

    for letter in dna:
        dna_compliment += compliment[letter]

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


### two names match if they're 2 letters off or less
def make_letter_freq_dict(name):
    letter_freq_dict = {}
    
    for char in name:
        letter_freq_dict[char] = letter_freq_dict.get(char, 0) + 1
    
    return letter_freq_dict

def is_close_match(name1, name2):
    """ Determine if two names match within 2 letters
    >>> is_close_match("Kristi", "Christi")
    True
    >>> is_close_match("Kristi", "Krystal")
    False
    """
    
    # first compare length to see if one is more than 2 characters longer
    if abs(len(name1) - len(name2)) > 2:
        return False
    
    
    name1_freq_dict = make_letter_freq_dict(name1) # {'K': 1, 'r': 1, 'i': 2, 's': 1, 't': 1}
    name2_freq_dict = make_letter_freq_dict(name2) # {'C': 1, 'h': 1, 'r': 1, 'i': 2, 's': 1, 't': 1}
    
    name1_missing_letters = []
    name2_missing_letters = []
    
    for key in name1_freq_dict:
        if key not in name2_freq_dict:
            name2_missing_letters.append(key)
            
    
    for key in name2_freq_dict:
        if key not in name1_freq_dict:
            name1_missing_letters.append(key)
            
    return len(name1_missing_letters) <= 2 and len(name2_missing_letters) <= 2
        
####### Make tic-tac-toe ##########

# Board as array of arrays 
# Ex: [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1]

# to create board:


class TicTacToeBoard:

    def __init__(self):
        self.board = [[0] * 3 for n in range(3)]
        game_won = False
        
    def print_board(self):
        for row in self.cells:
            print(row)
            
    def move_piece(self, player, row, col):
        
        # move piece to specified location

        #check if location is open
        assert self.board[row][col] == 0, "Cell is not open, try again"
        assert row < 3 and col < 3, "Cell is off the board, try again"

        
        # update cell
        self.board[row][col] = player

        self.game_won = is_winner()


    def is_winner(self):

       
#         # move piece to specified location
#         # check if win
#         # check if board is full
#         # print board

tic = TicTacToeBoard()
while not tic.game_won:
    player = input("What player are you? \n")
    row = input("What row?")
    col = input("What column?")
    tic.move_piece(player, row, col)
# tic.print_board()


####### Panagram ########
# A pangram is a sentence that contains all the letters of the English alphabet at least once, 
# like “The quick brown fox jumps over the lazy dog.”

# Write a function to check a sentence to see if it is a pangram or not.

def is_pangram(sentence):
    """ Determine if the sentence is a panagram 

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True

    >>> is_pangram("I like cats, but not mice")
    False
    """

    # get rid of spaces and punctuation
    # Edges: deal with spaces, non-alpha characters, and capital letters
    just_chars = set(''.join(char for char in sentence if char.isalpha()).lower())
    
    if len(just_chars) == 26:
        return True

    return False

    # Hackbright solution
    # used = {char.lower() for char in sentence if char.isalpha()}
    # return len(used) == 26

###### Pig Latin ######
# Turn a phrase into pig latin. There will be no punctuation.
# If the word begins with a consonant (not a, e, i, o, u), move the first letter to the end and add ‘ay’
# If the word begins with a vowel, add ‘yay’ to the end

#def pig_latin(phrase):
    """ Turn a phrase into pig latin.

    >>> pig_latin('porcupines are cute')
    'orcupinespay areyay utecay'

    >>> pig_latin('give me an apple')
    'ivegay emay anyay appleyay'
    """

    # will want to handle each word separately (turn into a list of words)
    # rearrange each word according to rules (loop over list with conditionals)
    # add each rearranged word to new list (append)
    # make list back into a sentence (" ".join(","))
    # Edges: capital letters

    # word_lst = phrase.split()
    # pig_latin_lst = []

    # for word in word_lst:
    #     if word[0] in {"a", "e", "i", "o", "u"}:
    #         pig_latin_lst.append(f"{word}yay")
    #     else:
    #         pig_latin_lst.append(f"{word[1:]}{word[0]}ay")

    # return " ".join(pig_latin_lst)

    ## Hackbright solution used a helper function

def make_pig_latin_word(word):
    """ Helper function to turn a word into pig latin"""
    if word[0] in {"a", "e", "i", "o", "u"}:
        return word + "yay"
    else:
        return word[1:] + word[0] + "ay"

def pig_latin(phrase):
    """ Turn a phrase into pig latin.

    >>> pig_latin('porcupines are cute')
    'orcupinespay areyay utecay'

    >>> pig_latin('give me an apple')
    'ivegay emay anyay appleyay'
    """

    word_lst = phrase.split()
    pig_latin_lst = [make_pig_latin_word(word) for word in word_lst]
    
    return " ".join(pig_latin_lst)


#### Prime Number Generator #####
# A prime number is a number >= 2 that is only evenly divisible by itself and 1.

# So, for example, 3 is a prime number but 4 (divisible by 2) is not. The first 
# few primes are: 2, 3, 5, 7, 11.

# Write a function that produces count prime numbers, where count is a value passed 
# into the function.

def is_prime(num):
    """ Determine if a number is prime."""

    # This counts on the range function not working if num is 2, which defaults to True
    # This also goes through all numbers sequentially O(n)
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True



def primes(count):
    """Return count number of prime numbers, starting at 2.
    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]
    """

    # need a helper function that generates prime numbers
        # how do you mathematically determine if a number is prime?
        # even numbers that are not 2 are automatically not prime (exclude evens)
        # that leaves odd numbers 3, 5, 7, 9. 
        # if a number is divisible by 9 then it's automatically divisible by 3 as well so get rid of 9
        # that leaves 3, 5, 7
        # I know there's a better way to do this, but I can't think of it.


    prime_lst = []
    num = 2
    while len(prime_lst) < count:
        if is_prime(num):
            prime_lst.append(num)
        num += 1

    return prime_lst


######## Print Digits Backwards ########


def print_digits(num):
    """ Print digits in reverse

    >>> print_digits(1)
    1
    >>> print_digits(314)
    4
    1
    3
    >>> print_digits(12)
    2
    1
    """

    # make string into a list of characters
    # reverse list
    # loop over list, printing each character

    # problem with this is that is prints the ints as 
    # strings.
    # reversed_nums = reversed(str(num))
    # for num in reversed_nums:
    #     print(num)

    # Hackbright solution
    while num:
        next_digit = num % 10
        print(next_digit)
        num = (num - next_digit) // 10


####### Print list recursively #########

def print_recursively(lst):
    """ Print a given list (lst) recursively

    >>> print_recursively([1, 2, 3])
    1
    2
    3
    """

    # base case: when the list is empty
    if not lst:
        return

    print(lst[0])
    print_recursively(lst[1:])
    return

    # Hackbrights solution

    # if lst:
    #     print(lst[0])
    #     print_recursively([1:])


####### Recursive Index #########
def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

    >>> recursive_index("hey", ["hey", "there", "you"])
    0

    >>> recursive_index("you", ["hey", "there", "you"])
    2
    """

    # Base case is when list is empty
    # need to keep track of the index. how?
    # need to shrink the list as we go

    # What's the base case?
    # How are you going to move forward?
    # 
    
    def _recursive_index(needle, haystack, start_at):

        # Check if not found (we've gone too far)
        if start_at == len(haystack):
            return None

        # Have we found it?
        if haystack[start_at] == needle:
            return start_at

        return _recursive_index(needle, haystack, start_at + 1)

    return _recursive_index(needle, haystack, 0)

######## Remove Duplicates #########
# write a function that is given a list of items and returns a new list of those items, 
# in the same order, but with duplicate removed.

def deduped(items):
    """Return new list from items with duplicates removed.
    >>> deduped([1, 1, 1])
    [1]
    >>> deduped([1, 2, 1, 1, 3])
    [1, 2, 3]
    >>> deduped([1, 2, 3])
    [1, 2, 3]
    >>> deduped([])
    []
    >>> a = [1, 2, 3]
    >>> b = deduped(a)
    >>> a == b
    True

    >>> a is b
    False
    """

    # create a new list
    # create a set of the list for fast lookup
    # Loop over current list and check if

    #### Solution 1 - all tests pass, but O(n^2) because
    #### for loop is O(n) and nested lookup of item in deduped_lst is
    #### also O(n)
    # deduped_lst = []
    # for item in items:
    #     if item not in deduped_lst:
    #         deduped_lst.append(item)

    # return deduped_lst

    #### Solution 2 - all tests pass,but won't because doesn't maintain order
    #return list(set(items))

    #### Hackbright Solution ######
    deduped_lst = []
    visited = set()

    for item in items:
        if item not in visited:
            deduped_lst.append(item)
            visited.add(item)

    return deduped_lst


###### Remove Linked List Node ######

class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_string(self):
        """Represent data for this node and it's successors as a string.

        >>> Node(3).as_string()
        '3'

        >>> Node(3, Node(2, Node(1))).as_string()
        '321'
        """

        out = []
        current = self

        while current:
            out.append(str(current.data))
            current = current.next

        return "".join(out)

def remove_node(node):
    """Given a node in a linked list, remove it.

    Remove this node from a linked list. Note that we do not have access to
    any other nodes of the linked list, like the head or the tail.

    Does not return anything; changes list in place.
    >>> ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))  # 1->2->3->4->5
    >>> three_node = ll.next.next
    >>> remove_node(three_node)
    >>> ll.as_string()
    '1245'

    >>> ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))  # 1->2->3->4->5
    >>> one_node = ll
    >>> remove_node(one_node)
    >>> ll.as_string()
    '2345'
    """

    # if Node 3 is deleted, Node 2's next must be updated to Node(3)'s next'

    # can update given node's data to the next node's data
    # can update given node's next to the next node's next

    node.data = node.next.data
    node.next = node.next.next


######## Reverse Linked List in place #########

class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_string(self):
        """Represent data for this node and it's successors as a string.

        >>> Node(3).as_string()
        '3'

        >>> Node(3, Node(2, Node(1))).as_string()
        '321'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)

def reverse_linked_list(head):
    """Given LL head node, return head node of new, reversed linked list.

    >>> ll = Node(1, Node(2, Node(3)))
    >>> new_ll = reverse_linked_list(ll)
    >>> new_ll.as_string()
    '321'
    """
    # 1 -> 2 -> 3

    # 3 -> 2 -> 1

    ### My solution reverses the LL in place.
    current = head
    second_curr = current.next
    third_curr = current.next.next

    while second_curr.next:
        if current == head:
            current.next = None

        second_curr.next = current
        current = second_curr

        if second_curr.next:
            second_curr = third_curr

        if second_curr.next:
            third_curr = second_curr.next

    second_curr.next = current
    head = second_curr

    return head


    ##### HB's solution ######
    prev = None
    curr = lst.head

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    lst.head = prev



#### Reverse Linked List ######


    ### HB's solution creates a second LL ####
    ### code is more succinct, but it takes up more memory than mine.
    ### Not sure which is better
    out_head = None
    n = head

    while n:
        out_head = Node(n.data, out_head)
        n = n.next

    return out_head


###### Reverse a string recursively ######

def rev_string(astring):
    """Return reverse of string using recursion.

    You may NOT use the reversed() function!
    >>> rev_string("porcupine")
    'enipucrop'
    """

    def _rev_string(astring, rev_string=""):

        if not astring:
            return rev_string

        rev_string += astring[-1]
        return _rev_string(astring[:-1], rev_string)

    return _rev_string(astring)


    ### HB Solution ###
    # if len(astring) < 2:
    #         return astring

    #     return astring[-1] + rev_string(astring[:-1])


########## Show even numbers ##########
def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list.
    >>> lst = [1, 2, 3, 4, 6, 8]
    >>> show_evens(lst)
    [1, 3, 4, 5]
    """
    even_indices = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            even_indices.append(i)

    return even_indices

    

############ Sort Sorted Lists ##########

def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    >>> a = [1, 3, 5, 7]
    >>> b = [2, 6, 8, 10]
    >>> sort_ab(a, b)
    [1, 2, 3, 5, 6, 7, 8, 10]
    """

    # This solution uses a lot of memory because slices are used 
    # sorted_lst = []

    # while a or b:
    #     if a == []:
    #         sorted_lst.extend(b)
    #         return sorted_lst
    #     elif b == []:
    #         sorted_lst.extend(a)
    #         return sorted_lst

    #     if a[0] < b[0]:
    #         sorted_lst.append(a[0])
    #         a = a[1:]
    #     else:
    #         sorted_lst.append(b[0])
    #         b = b[1:]


    ### HB solution better use of memory and works
    ### more like mergesort
    sorted_lst = []
    ia = 0
    ib = 0

    while ia < len(a) and ib < len(b):
        if a[ia] < b[ib]:
            sorted_lst.append(a[ia])
            ia += 1
        else:
            sorted_lst.append(b[ib])
            ib += 1

    sorted_lst.extend(a[ia:])
    sorted_lst.extend(b[ib:])

    return sorted_lst

####### Split a String #######

def split(astring, splitter):
    """Split a string by splitter and return list of splits.
    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']
    """
    # loop over indices of astring
    # Each loop, check if the char in astring is the first char in splitter
    # if not, move to the next letter in astring
    # if so, check if the next several letters in astring make up the splitter
    # if not, move to next letter in astring
    # if so, append the slice of astring

    split_lst = []
    start_index = 0
    i = 0

    while i < len(astring):
        if astring[i] == splitter[0]:
            split_test = astring[i: i + len(splitter)]
            if split_test == splitter:
                split_lst.append(astring[start_index: i])
                start_index = (i + len(splitter))
                i += len(splitter)
            else:
                i += 1
        
        else:
            i += 1
    split_lst.append(astring[start_index:])

    return split_lst

    #### HB Solution ###
    # def split(astring, splitter):
    # """Split a string by splitter and return list of splits."""

    # # START SOLUTION

    # out = []
    # index = 0

    # while index <= len(astring):

    #     curr_index = index
    #     index = astring.find(splitter, index)

    #     if index != -1:
    #         out.append(astring[curr_index:index])
    #         index += len(splitter)

    #     else:
    #         # couldn't find any more instances of splitter in astring
    #         out.append(astring[curr_index:])
    #         break

    # return out


######## Sum List Recursively #########

def sum_list(nums):
    """Using recursion, return the sum of numbers in a list.
    """
    if len(nums) == 0:
        return 0

    return nums[0] + sum_list(nums[1:])


    ### HB solution ###
    # if not nums:
    #     return 0

    # return nums[0] + sum_list(nums[1:])

######## Lazy Lemmings #########

def furthest(num_holes, cafes):
    """ Find the farthest any single lemming needs to travel for food.
        Lemmings can go backwards and forwards.
        Lemmings cannot loop around from last hole to the first
    """
    # >>> furthest(3, [0, 1, 2])
    # 0

    # >>> furthest(3, [2])
    # 2

    # >>> furthest(3, [0])
    # 2

    # >>> furthest(6, [2, 4])
    # 2

    # >>> furthest(7, [0, 6])
    # 3
    
    # Every hole is a cafe
    furthest = 0
    current_hole = 0
    distance_to_cafe = 0

    if num_holes == len(cafes):
        return furthest

    while current_hole < num_holes:
        if current_hole not in cafes:
            distance_to_cafe += 1
            if distance_to_cafe > furthest:
                furthest = distance_to_cafe
                distance_to_cafe = 0
        current_hole += 1

    return furthest

    #### solution attempt # 2
    for i in range(num_holes):
        for j in range(len(cafes)):
            if i < cafes[j]:
                distance = cafes[j] - i
                if distance > furthest:
                    furthest = distance


def furthest_optimized(num_holes, cafes):
    
    # >>> furthest_optimized(7, [0, 6])
    # 3

    # >>> furthest_optimized(3, [0, 1, 2])
    # 0

    # >>> furthest_optimized(3, [2])
    # 2

    # >>> furthest_optimized(3, [0])
    # 2

    # >>> furthest_optimized(6, [2, 4])
    # 2
    
    pass




#### Create a set #####

def create_set(lst):

    """
    """

    # in: [1, 1, 3, 4, 4, 4]
    # out: {1, 3, 4}

    no_duplicates = [lst[0]]
    # [1, 3, 4]

    new_set = {}

    for num in lst:
        new_set[num] = new_set.get(num, None)

    #     if num not in no_duplicates:
    #         no_duplicates.append(num)

    # for num in no_duplicates:
    #     new_set[num] = None

    return new_set


###### Counting Valleys ########

# Gary is an avid hiker. He tracks his hikes meticulously, paying close attention 
# to small details like topography. During his last hike he took exactly n  steps. 
# For every step he took, he noted if it was an uphill, U , or a downhill, D step. 
# Gary's hikes start and end at sea level and each step up or down represents a  
# unit change in altitude. We define the following terms:

# A mountain is a sequence of consecutive steps above sea level, starting with a 
# step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a 
# step down from sea level and ending with a step up to sea level.
# Given Gary's sequence of up and down steps during his last hike, find and print 
# the number of valleys he walked through.

# For example, if Gary's path is s = [DDUUUUDD], he first enters a valley 2  units deep. Then he 
# climbs out an up onto a mountain 2  units high. Finally, he returns to sea level 
# and ends his hike.

# Function Description

# Complete the countingValleys function in the editor below. It must return an integer 
# that denotes the number of valleys Gary traversed.

# countingValleys has the following parameter(s):

# n: the number of steps Gary takes
# s: a string describing his path
# Input Format

# The first line contains an integer , the number of steps in Gary's hike. 
# The second line contains a single string , of  characters that describe his path.

def countingValleys(n, s):

    sea_level = 0
    num_valleys = 0
    current = 0

    for step in s:
        if step == D:
            current += 1
        else:
            current -= 1

    pass


##### Check if parentheses are balanced #########

def is_balanced(string):
    """" Check if the parens in an equation are balanced 
    >>> is_balanced("{[]{()}}")
    True
    >>> is_balanced("[{}{}(]")
    False
    >>> is_balanced("(a+b)-(3*4))")
    False
    """
    parens_stack = []

    for char in string:
        if char == "(":
            parens_stack.append(char)

        if char == ")":
            if parens_stack:
                parens_stack.pop()
            else:
                return False

    if len(parens_stack) == 0:
        return True
    else:
        return False

        # if it's a closing parens:
            # if parens_stack empty, return false

####### Generate Minesweeper board ########

# > width = 8
# > height = 4
# > number_of_mines = 8
# > generate_board(width, height, number_of_mines)
# *112*100
# 123*3222
# 01**31**
# 013*2122

def generate_board(width, height, num_mines):
    """ Generate a 2d array with mines randomly placed and a number
        in each non-bomb position indicating the number of bombs
        that surround it.
    """
    board = [[0] * width for i in range(height)]

    mines = get_random_mine_positions(width, height, num_mines)
    #print(mines) # [[0, 1], [2, 0], [0, 3]]
    add_mines_nums(board, mines, height, width)



    return board


def print_board(board):
    """ Print board (2d array) with each inner array on a new line """
    for row in board:
        print(row)


def get_random_mine_positions(width, height, num_mines):
    """ Return a list of random coordinates in which to add a mine """

    # get coordinates for all positions in the board
    coords = [[x, y] for x in range(height) for y in range(width)]
    # randomly choose coordinates that have mines
    mine_positions = sample(coords, num_mines) #[[2, 1], [1, 2], [0, 2]]
    
    return mine_positions


def add_mines_nums(board, mine_positions, height, width):
    """ Add mines to board based on random coordinates for mines. """

    for mine_coord in mine_positions:
        row, col = mine_coord

        board[row][col] = "*"

        # cells surrounding the bomb
        row_range = range(row - 1, row + 2)
        col_range = range(col - 1, col + 2)

        # move through surrounding cells and add 1
        # for each cell that isn't a bomb
        for i in row_range:
            for j in col_range:
                if (0 <= i < height) and (0 <= j < width) and (board[i][j] != "*"):
                    board[i][j] += 1

    return board


board = generate_board(3, 4, 3)
print_board(board)


############## Two Sum ################

def two_sum(lst, sum):
    """ Given a lst and a number (sum), return a list of lists of pair
        in the lst that add up to the sum
    """
    result = []
    set_lst = set()


    for i in range(len(lst)):
        sum_minus_elem = sum - lst[i]

        if sum_minus_elem in set_lst:
            result.append([lst[i], sum_minus_elem])

        else: 
            set_lst.add(lst[i])

    return result




if __name__ == "__main__":
    import doctest
    
    result = doctest.testmod()
    if result.failed == 0:
        print("ALL TESTS PASSED")

    
    
    



