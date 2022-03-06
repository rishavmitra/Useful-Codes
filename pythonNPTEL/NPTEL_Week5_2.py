'''
Given a list of integers and a value k, print the number in the list that appears exactly k times. (It is guaranteed that there’s exactly one integer that appears k times).

Input Format:

First line of the input contains a list of integers

Second line of the input contains a value k

Output Format:

Display the number that appears exactly k times

Example:

Input:

1 2 2 3 3 3

3

Output:

3
'''
import numpy as np

List = list(map(int,input().split()))
x = np.array(List)

k = int(input())

unique, count = np.unique(x, return_counts=True) # This returns two values, unique and the count of the unique

Dict = dict(zip(unique,count)) # This zip() function zips the unique and count together.

for x,y in Dict.items():
    if(y == k):
        print(x)

