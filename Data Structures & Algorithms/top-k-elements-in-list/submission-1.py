from collections import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # O(N * log N) 
        # cnt = Counter(nums)
        # pq = []

        # for num, freq in cnt.items():
        #     heapq.heappush(pq, (freq, num))
        #     if len(pq) > k:
        #         heapq.heappop(pq)
        
        # res = []

        # for freq, num in pq:
        #     res.append(num)

        # return res
        
        n = len(nums)
        bucket = [[] for _ in range(1+n)] 

        cnt = Counter(nums)
        for num, freq in cnt.items():
            bucket[freq].append(num)
            

#        print(bucket)
        res = []
        remain = k

        for i in range(n, -1, -1):
            if not bucket[i]:
                continue
            if remain - len(bucket[i]) >= 0:
                remain -= len(bucket[i])
                for item in bucket[i]:
                    res.append(item)
            elif remain > 0:
                for j in range(remain):
                    res.append(bucket[i][j])

        return res
