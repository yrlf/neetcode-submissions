class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        ans = float('-inf')

        n = len(nums)

        for i in range(n):
            if nums[i] > total + nums[i]:
                total = nums[i]
            else:
                total = total + nums[i]
            ans = max(ans, total)
        
        return ans