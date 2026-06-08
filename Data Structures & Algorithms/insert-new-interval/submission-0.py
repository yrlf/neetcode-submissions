import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)

        # 1. 提取所有起点，用于二分查找插入位置
        left_bounds = [interval[0] for interval in intervals]
        
        # 2. 找到插入点并插入，保持 intervals 按 start 排序
        idx = bisect.bisect_left(left_bounds, newInterval[0])
        intervals.insert(idx, newInterval)
        
        res = []
        # 3. 线性扫描合并重叠区间
        # 此时 intervals 的长度变成了 n + 1
        for i in range(n + 1):
            curr = intervals[i]
            # 如果 res 为空，或者当前区间与 res 最后一个区间不重叠
            if not res or res[-1][1] < curr[0]:
                res.append(curr)
            else:
                # 发生重叠，更新 res 最后一个区间的终点为两者的最大值
                res[-1][1] = max(res[-1][1], curr[1])
        
        return res