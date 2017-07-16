
# Recursion: Davis' Staircase

# Davis has  staircases in his house and he likes to climb each staircase 1, 2, 3 steps at a time. Given the respective heights for 
# each of the  staircases in his house, find and print the number of ways he can climb each staircase on a new line.
# https://www.hackerrank.com/challenges/ctci-recursive-staircase

recordRec = [1,1,2] + [-1]*34
record = [1,1,2]

def countRec(x):
  if len(recordRec) > x and record[x] != -1: 
    return recordRec[x]
  else:
    recordRec[x] = countRec(x - 1) + countRec(x - 2) + countRec(x - 3)
    return recordRec[x]
    
def count(x):
  if len(record) > x:
    return record[x]
  else:
    for i in xrange(len(record)-1, x+1):
      record.append(record[-1] + record[-2] + record[-3])
  return record[x]

s = int(raw_input().strip())
for a0 in xrange(s):
    n = int(raw_input().strip())
    print countRec(n)

