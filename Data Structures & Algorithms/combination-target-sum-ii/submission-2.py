from functools import cache
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()
        n = len(candidates)

        def dfs(i, total, track):
            if i == n:
                if total == target:
                    output = ""
                    for each in track:
                        output += str(each) + ","
                    res.add(output)
                return
            
            dfs(i+1, total, track)
            if total < target:
                track.append(candidates[i])
                dfs(i+1, total + candidates[i], track)
                track.pop()
        

        dfs(0, 0, [])
        
        ans = []

        for s in res:
            tmp = []
            elements = s.split(",")
            for ele in elements:
                if ele:
                    tmp.append(int(ele))
            
            ans.append(tmp.copy())

        return ans