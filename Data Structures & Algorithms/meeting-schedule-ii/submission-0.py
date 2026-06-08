"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        events = []

        for i in range(len(intervals)):
            s = intervals[i].start
            e = intervals[i].end
            events.append((s,1))
            events.append((e,-1))
        

        events.sort()
        cnt = 0
        res = 0

        for x, typ in events:
            if typ == 1:
                cnt += 1
            else:
                cnt -= 1
            
            res = max(res, cnt)
        
        return res