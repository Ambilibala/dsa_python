def substring(n):   
    sum = 0
    w = 1
    n1=str(n)
    for i in range(len(n1) - 1, -1, -1):
        digit = int((n1[i]))
        sum = (sum + digit * w * (i + 1)) % (10**9 + 7 )
        w = (w * 10 + 1)
    return sum
n=int(input())
print(substring(n))

    
    #Logic
    #number converted to str tp iterate number from back. 
    #digits are taken. w is used used to calculate the weight of each digit.
    #(i+1) to calculate weight based on position