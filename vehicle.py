# Problem Statement – An automobile company manufactures both a two wheeler (TW) and a four wheeler (FW). A company manager wants to make the production of both types of vehicle according to the given data below:

# 1st data, Total number of vehicle (two-wheeler + four-wheeler)=v
# 2nd data, Total number of wheels = W
# The task is to find how many two-wheelers as well as four-wheelers need to manufacture as per the given data.

def count(n,w):
    x=w/2-n
    y=n-x
    print("tw is {x} and fw is{y}",x,y)
n=int(input("number"))
w=int(input("wheels"))
count(n,w)

    
    


