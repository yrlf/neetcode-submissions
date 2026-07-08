class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l, r = 0, n

        while l < r:
            mid = (l+r)//2

            if (nums[mid] > nums[-1] and target > nums[-1]) or (nums[mid]<=nums[-1] and target <= nums[-1]):
                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] > target:
                    l = mid + 1
                else:
                    r = mid
        
        if nums[l] != target:
            return -1
        else:
            return l