# string compression

# https://www.careercup.com/question?id=7449675
# asked by Yelp and Amazon

# Compress a given string "aabbbccc" to "a2b3c3" 
# constraint: inplace compression, no extra space to be used 
# assumption : output size will not exceed input size.. ex input:"abb" -> "a1b2" buffer overflow.. such inputs will not be given.

# https://www.hackerrank.com/challenges/string-compression

given = "abcaaabbb"
output = "abca3b3"

def compressor(given):

	
