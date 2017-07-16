
# given an array of integers and a number k, find the number of pairs in the array such that x + k = y

def  kDifference(a, k):
    dict = {}
    count = 0
    for x in a:
        if x not in dict:
            dict[x] = True
    print dict
    for x in a:
        if (x+k) in dict:
            count += 1
        if ((x-k) > 0) and (x-k) in dict:
            count += 1
    return count / 2
            
            