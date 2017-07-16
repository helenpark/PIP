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
  
