# Sorting

# http://danishmujeeb.com/blog/2014/01/basic-sorting-algorithms-implemented-in-python/

# 1. Bubble sort

# It’s basic idea is to bubble up the largest(or smallest), then the 2nd largest 
# and the the 3rd and so on to the end of the list. Each bubble up takes a full 
# sweep through the list.

def bubble_sort(items):
        for i in range(len(items)):
                for j in range(len(items)-1-i):
                        if items[j] &gt; items[j+1]:
                                items[j], items[j+1] = items[j+1], items[j]     

# 2. Insertion Sort

# Insertion sort works by taking elements from the unsorted list and inserting them 
# at the right place in a new sorted list. The sorted list is empty in the beginning. 
# Since the total number of elements in the new and old list stays the same, we can 
# use the same list to represent the sorted and the unsorted sections.

def insertion_sort(items):
        for i in range(1, len(items)):
                j = i
                while j &gt; 0 and items[j] &lt; items[j-1]:
                        items[j], items[j-1] = items[j-1], items[j]
                        j -= 1

# 3. Merge Sort

# Merge sort works by subdividing the the list into two sub-lists, sorting them using 
# Merge sort and then merging them back up. As the recursive call is made to subdivide 
# each list into a sublist, they will eventually reach the size of 1, which is 
# technically a sorted list.

def merge_sort(items):
        """ Implementation of mergesort """
        if len(items) &gt; 1:
 
                mid = len(items) / 2        # Determine the midpoint and split
                left = items[0:mid]
                right = items[mid:]
 
                merge_sort(left)            # Sort left list in-place
                merge_sort(right)           # Sort right list in-place
 
                l, r = 0, 0
                for i in range(len(items)):     # Merging the left and right list
 
                        lval = left[l] if l &lt; len(left) else None
                        rval = right[r] if r &lt; len(right) else None
 
                        if (lval and rval and lval &lt; rval) or rval is None:
                                items[i] = lval
                                l += 1
                        elif (lval and rval and lval &gt;= rval) or lval is None:
                                items[i] = rval
                                r += 1
                        else:
                                raise Exception('Could not merge, sub arrays sizes do not match the main array')
 

# 4. Quick Sort

# Quick sort works by first selecting a pivot element from the list. It then creates 
# wo lists, one containing elements less than the pivot and the other containing 
# elements higher than the pivot. It then sorts the two lists and join them with the 
# ivot in between. Just like the Merge sort, when the lists are subdivided to lists 
# of size 1, they are considered as already sorted

def quick_sort(items):
        """ Implementation of quick sort """
        if len(items) &gt; 1:
                pivot_index = len(items) / 2
                smaller_items = []
                larger_items = []
 
                for i, val in enumerate(items):
                        if i != pivot_index:
                                if val &lt; items[pivot_index]:
                                        smaller_items.append(val)
                                else:
                                        larger_items.append(val)
 
                quick_sort(smaller_items)
                quick_sort(larger_items)
                items[:] = smaller_items + [items[pivot_index]] + larger_items

# 5. Heap Sort

# This implementation uses the built in heap data structures in Python. To truly 
# understand haepsort, one must implement the heapify() function themselves. This 
# is certainly one obvious area of improvement in this implementation.

import heapq
 
def heap_sort(items):
        """ Implementation of heap sort """
        heapq.heapify(items)
        items[:] = [heapq.heappop(items) for i in range(len(items))]









