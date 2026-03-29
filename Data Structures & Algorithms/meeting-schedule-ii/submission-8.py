"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if len(intervals) == 1:
            return 1
        if len(intervals) == 0:
            return 0 
        s= []
        e = []
        for i in intervals:
            s.append(i.start)
            e.append(i.end)
        
        count =0 
        m = 0

        s.sort()
        e.sort()
        
        p1,p2 = 0,0

        while p1 != len(s)  and p2 != len(e):

            if s[p1] < e[p2]:
                count +=1
                p1+=1
            else:
                count -=1
                p2 +=1
            
            m = max(count,m)
    
        return m 

        

