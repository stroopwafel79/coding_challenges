# Is the word an anagram of a palindrome?
# A palindrome is a word that reads the same forward and backwards 
# (eg, “racecar”, “tacocat”). An anagram is a rescrambling of a word (eg for “racecar”, you could rescramble this as “arceace”).
# Determine if the given word is a re-scrambling of a palindrome.
# The word will only contain lowercase letters, a-z.

def make_dict(s):
    
    letter_dict = {}
    for letter in s:
        letter_dict[letter] = letter_dict.get(letter, 0) + 1

    return letter_dict


def is_anagram_of_palindrome(string):
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
