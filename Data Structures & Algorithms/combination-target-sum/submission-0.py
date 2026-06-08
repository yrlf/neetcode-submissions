class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)

        res = []

        def dfs(start, track):
            if sum(track) == target:
                res.append(track.copy())
                return

            if sum(track) > target:
                return


            for i in range(start, n):
                track.append(nums[i])
                dfs(i, track)
                track.pop()


        dfs(0, [])

        return res