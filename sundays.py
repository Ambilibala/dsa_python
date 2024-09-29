# Jack is always excited about sunday. It is favourite day, when he gets to play all day. And goes to 
# cycling with his friends.
# So every time when the months starts he counts the number of sundays he will get to enjoy. 
# Considering the month can start with any day, be it Sunday, Monday…. Or so on.
# Count the number of Sunday jack will get within n number of days.

def countsunday(day,d):
    no_of_week=d//7
    rem_days=d%7
    dicti={"sunday":0,"monday":1,"tuesday":2,"wednesday":3,"thursday":4,"friday":5}
    if(rem_days+dicti[day]<7):
        return(no_of_week)
    elif(rem_days+dicti[day]==7):
        return(no_of_week+1)
print(countsunday("monday",13))