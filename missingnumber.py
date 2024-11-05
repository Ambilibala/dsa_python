#finding the missing number

def missing(arr):
    a=[]
    for i in range(1,len(arr)):
        if i not in arr:
            return i
arr=[1,3,4,5,6]
print(missing(arr))


    

