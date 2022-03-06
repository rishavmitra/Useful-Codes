'''
Given a N X N square matrix, determine if it is a Symmetric Matrix.

Input Format:

The first line of the input contains an integer N which represents the number of rows and the number of columns.

Next N lines represent the elements of the matrix.

Output Format:

Print Yes or No

Example:

Input:

3

1 -2 3

-2 3 1

3 1 2

Output:

Yes
'''
import numpy as nd

N = int(input())
arr = []

for i in range(N):
    ar = list(map(int, input().split()))
    arr.append(ar)
arr = nd.array(arr)
t_arr = arr.transpose()
comparision = arr == t_arr


if comparision.all():
    print("Yes")
else:
    print("No")
