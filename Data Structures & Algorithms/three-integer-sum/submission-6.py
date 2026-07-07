class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def twoSum(start, end, target):
            print(start, end, target)
            res = []
            while start < end:
                i, j = start, end

                if nums[start] + nums[end] == target:
                    res.append([nums[start], nums[end]])
                    start += 1
                    end -= 1

                    while start < end and nums[i] == nums[start]:
                        start += 1
                
                    while end > start and nums[j] == nums[end]:
                        end -= 1

                elif nums[start] + nums[end] > target:
                    end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                

                
            
            return res

        n = len(nums)


        ans = []
        nums.sort()
        print(nums)
        i = 0
        while i < n:
            
            i0 = i
            target = - nums[i]
            res = twoSum(i+1, n-1, target)

            for each in res:
                each.append(nums[i])
                ans.append(each.copy())
            i+=1

            while i + 1 < n and nums[i] == nums[i0]:
                i+=1

        return ans

