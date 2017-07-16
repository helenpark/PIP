# Pramp

# https://www.pramp.com/question/7Lg1WA1nZqfoWgPbgM0M

# input:  arr = [8, 10, 2]
# output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]

# input:  arr = [2, 7, 3, 4]
# output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3]

def arrayOfArrayProducts(arr):
  result = []
  prod = 1
  for i in range(len(arr)):
    result.append(prod)
    prod *= arr[i]
    
  prod = 1
  for i in range(len(arr) - 1, 0, -1):
    result[i] *= prod
    prod *= arr[i]
    
  return result

print(arrayOfArrayProducts([8, 10, 2]))