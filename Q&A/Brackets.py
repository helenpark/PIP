# Brackets Question (Tony)

# Find all possible valid combination of brackets given a number of brackets possible
# e.g. 3 -> {}{}{}, {{{}}}, {}{{}}, {{}}{} -> 4

def brackets(p_arr, n):
  if (sum(p_arr) == n):
    print ''.join(['['*i + ']'*i for i in p_arr])
    return;

  for i in xrange(1, n - sum(p_arr)+1):
    brackets(p_arr + [i],n)

brackets([],8)