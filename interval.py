def canAttendMeetings(intervals)
        intervals.sort(key=lambda i:i.start)
        for i  in range(0,len(intervals)-1):
             i1=intervals[i]
             i2=intervals[i+1]
               
             if i1.end>i2.start:
                return False
        return True
