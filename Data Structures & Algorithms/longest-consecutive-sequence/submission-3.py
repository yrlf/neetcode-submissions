class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        
        start = set()

        for num in nums:
            if num - 1 in nums:
                continue
            start.add(num)
        
        res = 0
        for each in start:
            cnt = 1
            
            i = 1
            while each + i in nums:
                cnt += 1
                i += 1
            
            res = max(res, cnt)
        return res
        