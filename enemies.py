# Problem statement :

# There are some groups of devils and they splitted into people to kill them.
#  Devils make People to them left as their group and at last the group with maximum length will be killed. 
# Two types of devils are there namely “@” and “$”
# People is represented as a string “P”

def enemy(p):
    count=0
    for i in range(len(p)):
        if(p[i]=="@" or p[i]=="$"):
            count+=1
            if(p[0]=="@" or p[0]=="$"):
                break;
    return count
