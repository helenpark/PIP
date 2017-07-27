
import sys

def getCheapestCost(rootNode):

  # minCost = MAX_INT
  
  # if (len(rootNode.children) == 0):
  #   return rootNode
  
  # else:
  #   for i in xrange(len(rootNode.children)):
      
  #     tempCost = getCheapestCost(rootNode.child[i])
      
  #     if (tempCost < minCost):
  #         minCost = tempCost
  
  # return minCost + rootNode.cost


  print evalBranchCost(rootNode, root.cost, sys.maxint)
  # print(branchCosts)
  # return min(branchCosts)
 

def evalBranchCost(node, cost, minCost):
  
  print("node.cost", node.cost)
  print("cost", cost)
  print("minCost", minCost)
  
  if (len(node.children) == 0): #leaf
    minCost = min(cost+node.cost, minCost)
    print("new min: ", minCost)
    return minCost
    #return max(cost, maxCost)

  acc = cost + node.cost
  print("acc", acc)
  # branches out
  for child in node.children:
    print
    evalBranchCost(child, acc, minCost)



########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, cost, children=[]):
    self.cost = cost
    self.children = children
    self.parent = None

    
    
root = Node(0)

root.children = [Node(1, [Node(2), Node(4)]), Node(6, [Node(1)])]
  
print(getCheapestCost(root))