class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # [3,4,5,6,| 1,2] there will be 2 segments, last elemnt < first element if there is a rorate, check target in which segment
        # if target <= last element -> target is in 2nd segment
        # else target is in 1st segment


        n = len(nums)
        l, r = 0, n

        while l < r:
            mid = (l+r)//2

            if (target <= nums[-1] and nums[mid] <= target) or (target > nums[-1] and nums[mid] > nums[-1]): # same segment -> normal 
                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            else: # not in same segment
                if nums[mid] > nums[-1]:
                    l = mid + 1
                else:
                    r = mid
        

        if l < n and nums[l] == target:
            return l
        else:
            return -1

                
                



