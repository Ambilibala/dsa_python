def decimal(n):
    nstring=str(n)
    sum=0
    pow=0
    for i in range(len(nstring)-1,-1,-1):
        sum+=int(nstring[i])*(2**(pow))
        pow+=1
    return sum
n=int(input("entr the number"))
print(decimal(n))

