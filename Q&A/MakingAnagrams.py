# MakingAnagrams

# https://www.hackerrank.com/challenges/ctci-making-anagrams/submissions/code/29308263

# Given two strings,  and , that may or may not be of the same length, determine the minimum 
# number of character deletions required to make  and  anagrams. Any characters can be deleted 
# from either of the strings

def number_needed(a, b):
    dup_count = 0
    alphabet = [0]*26;
    counter = update_counter(b, update_counter(a, alphabet, True), False)
    
    #print counter
    for i in counter:
        if i == 0:
            continue
        else:
            dup_count += abs(i)
    return dup_count
    
    
    
def update_counter(word, counter, add):
    ascii_values = [ord(letter)-97 for letter in word]
    if add:
        for val in ascii_values:
            counter[val] += 1
        return counter
    else: 
        for val in ascii_values:
            counter[val] -=1    
        return counter
    
    
a = raw_input().strip()
b = raw_input().strip()
print number_needed(a, b)