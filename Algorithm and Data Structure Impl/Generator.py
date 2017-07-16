# Generator example

def square(nums):
	for i in nums:
		yield (i * i)

my_nums = square([1,4,2,5])

# OR: using comprehension

# comprehension
nums_comprehended = [x*x for x in [1,2,3,4]]
# becomes: generator
nums_generator = (x*x for x in [1,2,3,4])

print my_nums
print nums_comprehended
print nums_generator

print list(nums_generator)

