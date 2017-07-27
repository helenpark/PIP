#  CTCI: 4.3 (pg. 243)
# List of depths: gievn a binary tree, create a linked list 
# of all the nodes at each level
from collections import defaultdict

class Node:
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None

	#in-order: left, current, right
	def traverse(self,func, level=0):
		if self.left:
			self.left.traverse(func, level+1)
			func(self,level)    
		if self.right:
			self.right.traverse(func, level+1)

	def printNode(node, level):
		print level*'   '+`node.data`

	def test(): 
		t=create_tree(arr)
		t.traverse(printNode)
    	
	def create_tree(array):
		if (array==[]):
			return None
		mid = (len(array))/2
		node = TreeNode(array[mid])
		node.left = create_tree(array[0:mid])
		node.right = create_tree(array[mid+1:])
		return node

	def createListsFromTree3(treeNode):
	    d = defaultdict(list)
	    def fillDict(node, level):
	        d[level].append(node)
	    treeNode.traverse(fillDict)
	    return  d

listDepths()

# def listDepths(tree):
# 	visited = set()
# 	queue = [tree.root]
# 	while (queue):
# 		vertex = queue.pop()
# 		llist = LList()
# 		lnode = listNode()
# 		llist.head = lnode
# 		if vertex not in visited:
# 			lnode.val = vertex.value
# 			lnode.next = 

# 			visited.add(vertex)
# 			if vertex.left not in visited:
# 				queue.append(vertex.left)
# 			if vertex.right not in visited:
# 				queue.append(vertex.right)
# 	return


test = [1,4,7,9,14,20,21,24,71]

	
