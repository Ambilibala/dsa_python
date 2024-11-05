# def move(arr):
#     a=[]
#     c=0
#     n=len(arr)
#     for i in arr:
#         if i!=0:
#             c+=1
#             a.append(i)
#     for j in range(c,n):
#         a.append(0)
#     return a
# arr=[1,0,0,2,3,0,4,5]
# print(move(arr))
        

def move(arr):

    n = []
    zero_count = 0

    for element in arr:
        if element != 0:
            n.append(element)
        else:
            zero_count += 1

    return n + [0] * zero_count

arr = [1, 0, 0, 2, 3, 0, 4, 5]
print(move(arr))