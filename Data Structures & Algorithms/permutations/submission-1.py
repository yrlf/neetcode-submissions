class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = []
        seen = set()
        def dfs():
            #print(seen)
            if len(seen) == n:
                res.append(path.copy())
                return



            for j in range(n):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    path.append(nums[j])
                    dfs()
                    seen.remove(nums[j])
                    path.pop()
        
        dfs()
        return res