class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort(key = lambda x:(x[0], x[1]))

        n = len(intervals)

        def overlap(lastInterval, currInterval):
            return max(lastInterval[0], currInterval[0]) <= min(lastInterval[1], currInterval[1])

        for i in range(n):
            if len(res) == 0:
                res.append(intervals[i])
            else:
                if overlap(res[-1], intervals[i]):
                    res[-1][0] = min(intervals[i][0], res[-1][0])
                    res[-1][1] = max(intervals[i][1], res[-1][1])
                else:
                    res.append(intervals[i])
    
        return res