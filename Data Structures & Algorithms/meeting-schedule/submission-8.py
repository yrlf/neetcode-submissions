"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # intervals.sort(key = lambda x:x.start)
        # for i in range(1, len(intervals)):
        #     if max(intervals[i].start, intervals[i-1].start) < min(intervals[i].end, intervals[i-1].end):
        #         return False
        
        # return True

        events = []

        for i in range(len(intervals)):
            s = intervals[i].start
            e = intervals[i].end

            events.append((s, 1))
            events.append((e, -1))
        events.sort()
        cnt = 0
        print(events)
        for time, typ in events:
            if typ == 1:
                cnt += 1
            else:
                cnt -= 1
            
            if cnt > 1:
                return False
        
        return True