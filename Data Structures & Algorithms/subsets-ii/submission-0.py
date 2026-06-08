class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        track = []
        nums.sort()
        res = []
        def dfs(i):
            res.append(track.copy())

            for j in range(i, n):
                if j > i and nums[j] == nums[j-1]:
                    continue
                track.append(nums[j])
                dfs(j+1)
                track.pop()

        dfs(0)

        return res
