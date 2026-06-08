import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)

        left_bounds = [interval[0] for interval in intervals]
        
        idx = bisect.bisect_left(left_bounds, newInterval[0])
        intervals.insert(idx, newInterval)
        
        res = []

        for i in range(n + 1):
            curr = intervals[i]
            if not res or res[-1][1] < curr[0]:
                res.append(curr)
            else:
                res[-1][1] = max(res[-1][1], curr[1])
        
        return res