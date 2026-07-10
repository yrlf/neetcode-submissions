class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        n = len(nums)
        res = []

        def dfs(i, total, track):
            if total == target:
                res.append(track.copy())
                return
            if i == n or total > target:
                return

            dfs(i+1, total, track)

            track.append(nums[i])
            dfs(i, total + nums[i], track)
            track.pop()
        

        dfs(0,0, [])

        return res