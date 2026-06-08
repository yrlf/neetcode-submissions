class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        res = [[]]

        def dfs(i, track):
            if i == n:
                return

            track.append(nums[i])
            res.append(track.copy())
            dfs(i+1, track)
            track.pop()
            dfs(i+1, track)


        dfs(0, [])
        return res