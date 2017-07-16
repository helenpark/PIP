#Python List Functions


# filter
def f(x): return x % 3 == 0 or x % 5 == 0
filter(f, range(2, 25))

# map
def cube(x): return x*x*x
map(cube, range(1, 11))

def add(x, y): return x+y
map(add, seq, seq)

# List Comprehensions

# e.x. 1
squares = [x**2 for x in range(10)]

# e.x. 2
ex = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

