class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        n = len(nums)

        res = []

        seen = set()
        def dfs(i, track, seen): 
            if (len(track) == n):
                res.append(track.copy())
                return

            for i in range(n):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    track.append(nums[i])
                    dfs(i, track, seen)
                    track.pop()
                    seen.discard(nums[i])
                

        dfs(0, [], seen)

        return res