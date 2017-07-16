
# Reverse Array

def reverse_array(letters, first=0, last=None):
    "reverses the letters in an array in-place"
    if last is None:
        last = len(letters)
    last -= 1
    while first < last:
        letters[first], letters[last] = letters[last], letters[first]
        first += 1
        last -= 1

# Reverse string: reverse char but not order of words

def reverse_words(string):
	s='The dog ran'
	' '.join(w[::-1] for w in s.split())