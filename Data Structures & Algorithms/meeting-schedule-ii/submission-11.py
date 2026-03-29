"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s= []
        e = []
        for i in range(len(intervals)):
            s.append(intervals[i].start)
            e.append(intervals[i].end)

        s.sort()
        e.sort()

        p1,p2 = 0,0
        c,m= 0,0

        while p1 < len(intervals):

            if e[p2] <= s[p1]:
                p2+=1
                c-=1
            else:
                p1+=1
                c+=1
                m = max(m,c)
        
        return m
            



