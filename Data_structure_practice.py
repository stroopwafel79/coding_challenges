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

	def __repr__(self):
		return "<Binary Search Tree root: {}".format(self.root.data)


	def insert(self, data):
		# if no root make it this node
		if self.root == None:
			self.root = Node(data)

		else:
			self._insert(data, self.root)

	def _insert(self, data, curr_node):
		if data < curr_node.data:
			if curr_node.left_child == None:
				curr_node.left_child = Node(data)
			else:
				self._insert(data, curr_node.left_child)

		elif data > curr_node.data:
			if curr_node.right_child == None:
				curr_node.right_child = Node(data)
			else:
				self._insert(data, curr_node.right_child)

		else:
			print("Data already in tree!")


	def print_tree(self):
		""" Print tree using in-order tree traversal """
		if self.root != None:
			self._print_tree(self.root)

	def _print_tree(self, curr_node):
		if curr_node != None:
			self._print_tree(curr_node.left_child)
			print(curr_node.data)
			self._print_tree(curr_node.right_child)


tree = BinarySearchTree()
tree.insert(6)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(45)

tree.print_tree()
















