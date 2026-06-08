class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        l, r = 0, 0
        pq = deque()
        res = []

        while r < n:
            val = nums[r]

            while pq and r - pq[0] >= k:
                pq.popleft()

            while pq and val > nums[pq[-1]]:
                pq.pop()
            
            pq.append(r)

            r += 1

            while l < r and r - l > k:
                l += 1
            
            if (r - l == k):
                res.append(nums[pq[0]])

        
        return res