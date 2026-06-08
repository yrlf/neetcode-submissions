class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)
        
        nums1 = nums[1:]
        nums2 = nums[:-1]
        nums3 = nums[1:-1]


        memo = {}
        def dfs(i, data):
            if i in memo:
                return memo[i]
            m = len(data)
            if i >= m:
                return 0
            
            res = 0

            res = max(res, dfs(i+2, data) + data[i], dfs(i+1, data))

            memo[i] = res
            return res
        res = float('-inf')
        res = max(res, dfs(0, nums1))
        memo = {}
        res = max(res, dfs(0, nums2))
        memo = {}
        res = max(res, dfs(0, nums3))

        return res