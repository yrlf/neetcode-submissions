class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []

        # 1. 处理左侧完全不重叠的区间
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # 2. 合并重叠的区间
        # 这里的判断条件是：只要当前区间起点 <= 新区间（或合并中区间）的终点，就有重叠
        # 同时要保证 i < n 防止越界
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1]) # 注意这里是和 intervals[i][1] 比
            i += 1
        
        # 将合并后的（或原本的）newInterval 加入结果
        res.append(newInterval)

        # 3. 处理右侧完全不重叠的区间
        while i < n:
            res.append(intervals[i])
            i += 1

        return res