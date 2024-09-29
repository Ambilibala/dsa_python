
# def equilibrium(arr):
#     lsum = 0
#     rsum = 0
#     for i in range(len(arr)):
#         for k in range(i - 1):
#             lsum += arr[k]
#         for j in range(i + 1, len(arr)):
#             rsum += arr[j]
#         if lsum == rsum:
#             return i + 1
#     return -1

# arr = [2, 5, 3, 7, 0]
# print(equilibrium(arr))



def equilibriumPoint(arr):
    n = len(arr)

    for i in range(n):
        lsum = sum(arr[:i])  
        rsum = sum(arr[i+1:n+1])  
        if lsum == rsum:
            return i + 1
    return -1

arr = [2, 5, 3, 7, 0]
print(equilibriumPoint(arr))
