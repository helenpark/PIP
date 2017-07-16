#  MinimalTree

#  CTCI: 4.2 (pg. 242)
#  take sorted array with unique increasing integers, and build a bst with minimal height

#  input: [1,4,7,9,14,20,21,24,71]
#  output: []

class Node:
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None

class BST:
	def __init__(self):
		self.root = None

def minimalTree(arr, n):
	if n == 0:
		return None
	node = Node(arr[n/2])
	node.left = minimalTree(arr[:n/2], n/2)
	node.right = minimalTree(arr[n/2:], n/2)
	return node;

#  CTCI: 4.3 (pg. 243)
# List of depths: gievn a binary tree, create a linked list 
# of all the nodes at each level

def listDepths(tree):


test = [1,4,7,9,14,20,21,24,71]
print minimalTree(test, 9)
	
