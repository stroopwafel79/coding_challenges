####### Linked List ##########
class Node:
	""" Create Node class"""
	def __init__(self, data):
		# Each Node instantiated with data
		self.data = data
		self.next = None

class LinkedList:
	""" Create a LinkedList class"""
	def __init__(self):
		# Instantiate an empty node as the head when the LL instantiated.
		self.head = None
	

	def append(self, data):
		""" Add a node to the end of the LL"""
		new_node = Node(data)
		current = self.head

		if self.head is None: 
			self.head = new_node

		else:
			while current.next != None:
				current = current.next

			current.next = new_node
	
	def print_nodes(self):

		current = self.head
		
		while current:
			print(current.data)
			current = current.next

	def delete_node(self, data):

		current = self.head

		if current.data == data:
			self.head = self.head.next


######### Binary Search Tree ###########
""" Binary Search Tree:
		- Each node has only two children (left and right)
		- The left node is less than the parent node
		- The right node is greater than the parent node
"""
class Node:

	def __init__(self, data=None):
		self.data = data
		self.left_child = None
		self.right_child = None

class BinarySearchTree:

	def __init__(self, root=None):
		self.root = root


	def insert_node(self, data):
		# if no root make it this node
		if self.root == None:
			self.root = Node(data)

		# if there is a root check if data is > or < root.data
		elif data < self.root.data:
			













