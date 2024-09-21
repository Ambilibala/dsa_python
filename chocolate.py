# A chocolate factory is packing chocolates into the packets. The chocolate packets here represent 
# an array of N number of integer values. The task is to find the empty packets(0) of chocolate and 
# push it to the end of the conveyor belt(array)

def choco(arr):
    k=0
    for num in arr:
        if(num!=0):
            arr[k]=num
            k+=1
    for i in range(k,len(arr)-1):
        arr[i]=0
    return arr
a=[2,0,3,0,1,11,0]
print(choco(a))



           

