from collections import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        pq = []

        for num, freq in cnt.items():
            heapq.heappush(pq, (freq, num))
            if len(pq) > k:
                heapq.heappop(pq)
        
        res = []

        for freq, num in pq:
            res.append(num)

        return res