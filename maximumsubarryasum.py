# Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
# has the largest sum and returns its sum and prints the subarray.

def maxsum(arr,n):
    maxi=-~
    for i in range(1,n):
        for j in range(i,n):
            sum=0
    for k in range(i,j):
        maxi=max(sum,maxi)
    return maxi


