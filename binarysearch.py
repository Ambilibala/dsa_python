def binaryserach(arr,target):
    low=0
    high=len(arr)-1
    
    while(low<high):
        mid=low+high//2
        if(target==arr[mid]):
            return mid
        elif (target<arr[mid]):
            high=mid-1
        elif(target>arr[mid]):
            low=mid+1
    return -1
    
    
arr=[1,2,3,4,5,67,5]
target=int(input("enter teh target"))
result=print(binaryserach(arr,target))
if(result!=-1):
    print(f"target is at {result}")
else:
    print("target not found")

    
    