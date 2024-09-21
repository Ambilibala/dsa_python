def slide(arr,k):
    maxi=sum(arr[:k])
    window_sum=maxi
    n=len(arr)
    for i in range(n-k):
        window_sum=window_sum-arr[i]+arr[i+k]
        maxi=max(maxi,window_sum)
    return(maxi)
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(slide(arr,k))