class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = -1, n

        while l + 1 < r:
            m = (l+r)>>1
            if nums[m] >= target:
                r = m
            else:
                l = m
        
        if r < n and r >= 0 and nums[r] == target:
            return r
        else:
            return -1
