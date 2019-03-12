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

    # word lengths must be the same to be an anagram
    if len(word1) != len(word2):
        return False

    # make a letter frequency dictionary of each word
    d1 = hash_word(word1)
    d2 = hash_word(word2)
    
    # dictionary lengths mush be the same to be anagrams
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


######### Checkr Technical Screen ####Our live coding session consists 
# of a name matching exercise 
# that is the foundation of your success at Checkr. We found out quickly 
# this is a great indicator for future performance and success on the job. 
# The challenge will consist of verifying names in a given list. You will 
# have a few test cases to test your solution against and one bonus 
# transposition question.


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
        
####### Make a game board

# Board as array of arrays 
# Ex: [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1]

# to create board:


# class TicTacToeBoard:

#     def __init__(self):
#         self.cells = [[0] * 3 for n in range(3)]
        
#     def print_board(self):
#         for row in self.cells:
#             print(row)
            
#     def move_piece(self, player, x_axis, y_axis):
        
#         # move piece to specified location
#         if self.player == "X"
#             self.cells[y_axis][x_axis] = "X"
#         else:
#             self.cells[y_axis][x_axis] = "O"



        
#         # move piece to specified location
#         # check if win
#         # check if board is full
#         # print board

# tic = TicTacToeBoard()
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





if __name__ == "__main__":
    import doctest
    
    result = doctest.testmod()
    if result.failed == 0:
        print("ALL TESTS PASSED")

    
    
    



