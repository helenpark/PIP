# Array Rotation

# https://www.hackerrank.com/challenges/ctci-array-left-rotation

# A left rotation operation on an array of size  shifts each of the array's elements  unit to the left. 
# For example, if left rotations are performed on array , then the array would become .

# Given an array of  integers and a number, , perform  left rotations on the array. Then print the 
# updated array as a single line of space-separated integers.

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