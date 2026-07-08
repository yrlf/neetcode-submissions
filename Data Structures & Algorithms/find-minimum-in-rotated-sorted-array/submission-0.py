class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid
        
        
        return min(nums[-1], nums[l])