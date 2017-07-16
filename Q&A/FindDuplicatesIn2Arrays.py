# Pramp

# https://www.pramp.com/question/15oxrQx6LjtQj9JK9XlA

# input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]

# output: [3, 6, 7] # since only these three values are both in arr1 and arr2

def findDuplicates(arr1, arr2):
  
  curr1 = 0
  curr2 = 0
  ans = []
  
  while (curr1 <= len(arr1)-1) and (curr2 <= len(arr2)-1):
    #print("arr1: ", arr1[curr1])
    #print("arr2: ", arr2[curr2])
    if (arr1[curr1] == arr2[curr2]):
      #print("same")
      ans.append(arr1[curr1])
      curr1=curr1+1
      curr2=curr2+1
    
    elif (arr1[curr1] < arr2[curr2]):
      curr1 = curr1+1
    else:
      curr2 = curr2+1
  
  return ans

def findDfindDuplicates1(arr1, arr2):

  ans = []
  
  l1 = len(arr1)
  l2 = len(arr2)
  if (l1 < l2):
    for elem in arr1
      if search(elem, arr2):
        ans.append(elem)
  else:
    for elem in arr2
      if search(elem, arr1):
        ans.append(elem)
    
  return arr
  

arr1 = [1, 2, 3, 5, 6, 7]

arr2 = [3, 6, 7, 8, 20]

output = [3, 6, 7]

print(findDuplicates(arr1, arr2))