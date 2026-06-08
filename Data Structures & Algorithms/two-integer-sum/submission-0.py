class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # num2idx: num -> idx 
        # loop through nums, find need = target - nums[i], if in num2idx -> return the idx pair

        # TC: O(N), SC: O(N)

        num2idx = {}

        for i in range(len(nums)):
            need = target - nums[i]
            if need in num2idx:
                return [num2idx[need], i]
            
            if nums[i] not in num2idx:
                num2idx[nums[i]] = i
        
        return []




        