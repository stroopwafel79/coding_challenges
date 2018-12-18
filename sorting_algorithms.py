#### bubble sort - O(n^2)

# l = [ 7, 4, 2, 9, 3, 5]

# compare first 2 numbers, swap the big one to the right
def bubble_sort(lst):
	# makes sure it keeps looping
	for i in range(len(lst) - 1):
	# len(l) - 1 prevents a range error when comparing the last pair
	# len(l) - 1 - i stops checking the last ones because the larger nums
	# already bubbled to the top
		for j in range(len(lst) - 1 - i): # create 0, 1, 2, 3, 4, 5 
			if lst[j] > lst[j + 1]:
				lst[j], lst[j + 1] = lst[j + 1], lst[j]


### merge sort - O(nlogn)

def make_lst_of_1(lst):
	""" Break list down into a bunch of list of length 1 using recursion"""
	# base case is when the list is length 1 so return that
	if len(lst) < 2:
		return(lst)

	mid = len(lst) // 2

	lst1 = make_lst_of_1(lst[:mid])
	lst2 = make_lst_of_1(lst[mid:])

	return merge_sort(lst1, lst2)


def merge_sort(lst1, lst2):

	sorted_lst = []

	while len(lst1) > 0 or len(lst2) > 0:
		if lst1 == []:
			sorted_lst.append(lst2.pop(0))

		elif lst2 == []:
			sorted_lst.append(lst1.pop(0))

		elif lst1[0] > lst2[0]:
			sorted_lst.append(lst1.pop(0))

		else:
			sorted_lst.append(lst2.pop(0))

	return sorted_lst








if __name__ == '__main__':
	
	l = [ 7, 4, 2, 9, 3, 5]
	bubble_sort(l)
	make_lst_of_1(l)