# PRAMP

# https://www.pramp.com/question/W5EJq2Jld3t2ny9jyZXG
# input:  document = "Practice makes perfect. you'll only
#                     get Perfect by practice. just practice!"

# output: [ ["practice", "3"], ["perfect", "2"],
#           ["makes", "1"], ["get", "1"], ["by", "1"],
#           ["just", "1"], ["youll", "1"], ["only", "1"] ]

# my solution:

import string
import operator


def wordCountEngine(document):
  
  counter = {}
  words = document.translate(None, string.punctuation).lower().split()
  
  for word in words:
    
    if word in counter:
      counter[word] = counter[word] + 1
    else:
      counter[word] = 1
      
  counter = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)
  print(counter)
  return
    
 
wordCountEngine("Practice makes perfect. you'll only get Perfect by practice. just practice!")

# Not my solution!
def wordCountEngine(document):
  # O(N) to creat arr
  # O(N) to filter out punctuations
  # O(M) to create array of counts
  # O(M log M) for sort
  
  # TIME: O(N+M log M)
  # SPACE: O(M)
  doc_arr = document.split()
  
  punctuations = {"!", "?", ".", ",", ":", ";", "'"}
  
  tally = {}
  
  for word in doc_arr:
    formatted_word = word.lower()
    temp_word = ""
    for char in formatted_word:
      if char not in punctuations:
        temp_word = temp_word + char
    if temp_word not in tally:
      tally[temp_word] = 1
    else:
      tally[temp_word] += 1
  
  # ['perfect', '2'], ['just', '1'], ['get', '1'], ['makes', '1']
  
  output = [[word, str(count)] for word, count in tally.items()]
  
  output.sort(key=operator.itemgetter(1), reverse=True)
  
  return output

document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
print(wordCountEngine(document))

#key=operator.itemgetter(1)


  # init the word counter list of lists.
    # Since, in the worst case scenario, the
    # number of lists is going to be as
    # big as the maximum occurrence count,
    # we need counterList's size to be the
    # same to be able to store these lists.
    # Creating counterList will allow us to
    # “bucket-sort” the list by word occurrences
    counterList = new Array(largestCount+1)
    for j from 0 to largestCount:
        counterList[j] = null

    # add all words to a list indexed by the
    # corresponding occurrence number.
    for word in wordMap.keys():
        counter = wordMap[word]
        wordCounterList = counterList[counter]

        if (wordCounterList == null):
            wordCounterList = []

        wordCounterList.push(word)
        counterList[counter] = wordCounterList

    # iterate through the list in reverse order
    # and add only non-null values to result
    result = []
    for l from counterList.length-1 to 0:
        wordCounterList = counterList[l]
        if (wordCounterList == null):
            continue

        stringifiedOccurrenceVal = toString(l)
        for m from 0 to wordCounterList.length-1:
            result.push([wordCounterList[m], stringifiedOccurrenceNum])
