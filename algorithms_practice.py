##### Sieve of Eratosthenes #######

def sieve_of_eratosthenes(num):
    """ Return a list of all prime numbers smaller than or equal to num.

    >>> sieve_of_eratosthenes(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    >>> sieve_of_eratosthenes(20)
    [2, 3, 5, 7, 11, 13, 17, 19]

    >>> sieve_of_eratosthenes(6)
    [2, 3, 5]

    """
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(num + 1)] # num + 1 b/c want up to and INCLUDING num
    # for 6 -> [True, True, True, True, True, True, True]
    prime_lst = []

    p = 2

    ### Changes the prime list above
    while p * p <= num: # is this only going up to the square root of num? If so, why?
    # for 6 (p=2) -> 2*2=4 -> 4 IS <= 6
    # for 6 (p=3) -> 3*3=9 -> 9 IS NOT <= 6
        if prime[p] == True:
            # update all multiples of p
            for i in range(p * 2, num + 1, p): 
            # for 6 -> for i in range(4, 7, 2) -> (4, 6) -> these turn to False
            # for 6 -> [True, True, True, True, False, True, False]
                prime[i] = False

        p += 1
        
    for i in range(2, num):
        if prime[i] == True:
            prime_lst.append(i)

    return prime_lst

####### Binary Search #######

def binary_search(target, nums):
    """ Determine if target is present in a SORTED list of nums."""
    

if __name__ == '__main__':
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print("ALL TESTS PASSED")
