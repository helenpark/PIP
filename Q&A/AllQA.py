
# Stock Max Difference

# Given an array of ints, determine the max profit from buying
# and selling once each. You must buy before you sell. if the array continuously 
# decreases, return -1.

def maxDifference( a):
    maxDiff = -1
    low = a[0]
    
    for i in a[1:]:
        if i - low > maxDiff: maxDiff = i - low 
        if i < low: low = i
            
    return maxDiff

# Time Complexity: Primality

# If possible, try to come up with an  primality algorithm, or see what 
# sort of optimizations you can come up with for an  algorithm.
# https://www.hackerrank.com/challenges/ctci-big-o/copy-from/30793312

import math

def isPrime(n):
    if n == 2:
        return True
    elif n == 1 or (n & 1) == 0:
        return False
    
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    
    return True

p = int(input())
for i in range(0, p):
    x = int(input())
    
    s = "Prime" if (isPrime(x)) else "Not prime"
    print(s);


# DFS: Connected Cell in a Grid

# Given an n x m matrix, find and print the number of cells in the largest region in the 
# matrix. Note that 
# there may be more than one region in the matrix.
# https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid

def get_biggest_region(grid):
  def bfs(grid, x, y):
    queue = [[x,y]]
    start, end = 0, 1
    
    while (start < end):
      for pos in xrange(start, end):
        curPos = queue[pos]
        for i in xrange(-1,2):
          for j in xrange(-1, 2):
            aX, aY = curPos[0] + i, curPos[1] + j

            if [aX, aY] not in queue and -1 < aY < len(grid) \
            and -1 < aX < len(grid[0]) and grid[aY][aX]:
              queue.append([aX, aY])
              grid[aY][aX] = 0
      start = end
      end = len(queue)
      
    return len(queue)
  
  maxReg = 0
  
  for y in xrange(len(grid)):
    for x in xrange(len(grid[0])):
      if grid[y][x]:
        maxReg = max(maxReg, bfs(grid, x, y))
  
  return maxReg
      
n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid)


# Recursion: Davis' Staircase

# Davis has  staircases in his house and he likes to climb each staircase 
# 1, 2, 3 steps at a time. Given the respective heights for 
# each of the  staircases in his house, find and print the number of ways 
# he can climb each staircase on a new line.
# https://www.hackerrank.com/challenges/ctci-recursive-staircase

recordRec = [1,1,2] + [-1]*34
record = [1,1,2]

def countRec(x):
  if len(recordRec) > x and record[x] != -1: 
    return recordRec[x]
  else:
    recordRec[x] = countRec(x - 1) + countRec(x - 2) + countRec(x - 3)
    return recordRec[x]
    
def count(x):
  if len(record) > x:
    return record[x]
  else:
    for i in xrange(len(record)-1, x+1):
      record.append(record[-1] + record[-2] + record[-3])
  return record[x]

s = int(raw_input().strip())
for a0 in xrange(s):
    n = int(raw_input().strip())
    print countRec(n)


# Time Complexity: Primality

# If possible, try to come up with an  primality algorithm, or see what 
# sort of optimizations you can come up with for an  algorithm.
# https://www.hackerrank.com/challenges/ctci-big-o/copy-from/30793312

import math






def isPrime(n):
    if n == 2:
        return True
    elif n == 1 or (n & 1) == 0:
        return False
        
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    
    return True

p = int(input())
for i in range(0, p):
    x = int(input())

    s = "Prime" if (isPrime(x)) else "Not prime"
    print(s);
# Sorting Comparator

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return 'player(name=%s, score=%s)' % (self.name, string(self.score))
 
        
    def comparator(a, b):
        if a.score == b.score:
            if a.name < b.name:
                return -1
            else:
                return 1
        else:
            if  a.score < b.score:
                return 1
            else:
                return -1





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
    
# HackerRank: CTCI
# Tree: is this a BST




def check_binary_search_tree_(root):
    arr = []
    count = 0
    arr = inorderTraversal(root, arr)
    if ((sorted(arr)) == arr) and (len(set(arr)) == len(arr)):
        return True
    else:
        return False

def inorderTraversal(root, arr):
    if root != None:
        inorderTraversal(root.left, arr)
        arr.append(root.data)
        inorderTraversal(root.right, arr)
    return arr
  


# given an array of integers and a number k, find the number of pairs 
# in the array such that x + k = y

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
            
            
# MakingAnagrams

# https://www.hackerrank.com/challenges/ctci-making-anagrams/submissions/code/29308263

# Given two strings,  and , that may or may not be of the same length, 
# determine the minimum number of character deletions required to make  and  
# anagrams. Any characters can be deleted from either of the strings

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
# Array Rotation

# https://www.hackerrank.com/challenges/ctci-array-left-rotation

# A left rotation operation on an array of size  shifts each of the array's 
# elements  unit to the left. 
# For example, if left rotations are performed on array , 
# then the array would become .

# Given an array of  integers and a number, , perform  left rotations on the array.
# Then print the updated array as a single line of space-separated integers.

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static int[] arrayLeftRotation(int[] a, int n, int k) {
        int[] shifted = new int[a.length];
        for (int i=0; i<a.length; i++) {
            if (i-k < 0) {
                shifted[a.length - (k-i)] = a[i];
            } else {
                shifted[i-k] = a[i];
            }
        }
        return shifted;
    }
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int a[] = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
      
        int[] output = new int[n];
        output = arrayLeftRotation(a, n, k);
        for(int i = 0; i < n; i++)
            System.out.print(output[i] + " ");
      
        System.out.println();
      
    }
}
# string compression

# https://www.careercup.com/question?id=7449675
# asked by Yelp and Amazon

# Compress a given string "aabbbccc" to "a2b3c3" 
# constraint: inplace compression, no extra space to be used 
# assumption : output size will not exceed input size.. ex input:"abb" -> 
# "a1b2" buffer overflow.. such inputs will not be given.

# https://www.hackerrank.com/challenges/string-compression

given = "abcaaabbb"
output = "abca3b3"

def compressor(given):


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
# Fibonacci


## Example 1: Using looping technique
def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a
print fib(5)
 
## Example 2: Using recursion
def fibR(n):
 if n==1 or n==2:
  return 1
 return fib(n-1)+fib(n-2)
print fibR(5)
 
