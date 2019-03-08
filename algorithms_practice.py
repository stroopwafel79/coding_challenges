##### Sieve of Eratosthenes #######

def sieve_of_eratosthenes(num):
    """ Return a list of all prime numbers smaller than or equal to num."""
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

    floor_index = -1
    ceiling_index = len(nums)

    # as long as there's at least one index between floor and ceiling
    # when this is false, the list has been exhausted and the target
    # is not present.
    while floor_index + 1 < ceiling_index:
        mid_index = (ceiling_index - floor_index) // 2
        guess_index = floor_index + mid_index
        guess_value = nums[guess_index]

        if guess_value == target:
            return True

        if guess_value > target:
            ceiling_index = guess_index

        else:
            floor_index = guess_index

    return False


##### Binary Search ######

def merge_sort(lst_to_sort):
    """ Sort a list """

    # Base case: an empty list or one with one element is automatically sorted.
    if len(lst_to_sort) < 2:
        return lst_to_sort

    # Step 1: divide list in half
    mid_index = len(lst_to_sort) // 2
    left = lst_to_sort[: mid_index]
    right = lst_to_sort[mid_index :]

    # Step 2: sort each half
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # Step 3: merge sorted halfs together
    sorted_lst = []
    curr_index_left = 0
    curr_index_right = 0

    while len(sorted_lst) < len(left) + len(right):
        # current left index is within the bounds of the left list
        if (curr_index_left < len(left) and
                # TODO test if you can reword as len(right) == 0
                # Is this testing if the right list is empty?
                (curr_index_right == len(right) or
                # 1st elem in left < 1st elem in right
                 sorted_left[curr_index_left] < sorted_right[curr_index_right]
                )
            ): 
            sorted_lst.append(sorted_left[curr_index_left])
            curr_index_left += 1

        else:
            sorted_lst.append(sorted_right[curr_index_right])
            curr_index_right += 1

    return sorted_lst










if __name__ == '__main__':
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print("ALL TESTS PASSED")
