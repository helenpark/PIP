"""
Diego, Chile
Helen, Canada


grantsArray = [2, 100, 50, 120, 1000]
              [2, 47, 47, 47, 47]
              
              [40, 100, 50, 120, 1000]
              [38, 38, 38, 38, 38]


              [2, 40, 50, 120, 1000]
              [2, ]
              
              
              [1, 37, 50, 66, 1000]
              
              base = 38
              
              
              
newBudget = 190
190/5 = 38 -> base
38*4 + 2 = 154 # check below base 2.
190-154/4 = 9 
9+38 = 47 # potential

# check if the number is below potential, treat as case 2. 


38*3 + 2 + 40 = 156
190-156/3 = 11.3
11.3+38 = 


output 47



"""
def find_grants_cap(grantsArray, newBudget):
  
  n = len(grantsArray)
  numBelowBase = 0
  belowBaseAmt = 0
  base = newBudget/n
  totalUsed = 0
  
  #print(base)
  
  for grant in grantsArray:
    
    if grant < base:
      numBelowBase = numBelowBase + 1
      belowBaseAmt = belowBaseAmt + grant
   
  #print(numBelowBase)
  ppbudget = (newBudget - (base * (n-numBelowBase) + belowBaseAmt))/(n-numBelowBase) + base
  
  return ppbudget
    
  
  
grantsArray = [2, 100, 50, 120, 1000]

print(find_grants_cap(grantsArray, 190))
  