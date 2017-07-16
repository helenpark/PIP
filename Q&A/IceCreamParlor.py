# Binary Search: Ice Cream Parlor

def pick2(m, costs):
    d = {}
    for i in xrange(len(costs)):
        #print str(costs[i])
        #print d
        if costs[i] in d:
            print (str(d[costs[i]] + 1) + " " + str(i+1))
        else:
            d[m-costs[i]] = i
        
        
t = int(raw_input().strip())
for a0 in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    pick2(m, a)
    