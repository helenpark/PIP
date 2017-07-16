# Binary trees: each node has no more than two child nodes

# BST: ordering property 
# -> left is less than node
# -> right is greater than node

# Balanced vs Unbalanced

# Traversal:
# 1. pre-order:
# -> root, left, right
# 2. in-order:
# -> left, root, right
# 3. post-order:
# -> left, right, root

# BST IMPLEMENTATION 

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

# HackerRank: CTCI
# Tree: is this a BST


def check_binary_search_tree_(root):
    arr = []
    count = 0
    arr = inorderTraversal(root, arr)
    if ((sorted(arr)) == arr) and (len(set(arr)) == len(arr)):
        return True
    else:
        return False

def inorderTraversal(root, arr):
    if root != None:
        inorderTraversal(root.left, arr)
        arr.append(root.data)
        inorderTraversal(root.right, arr)
    return arr



