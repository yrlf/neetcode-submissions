class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        
        def dfs(i, j):


            grid[i][j] = "0"
            res = 1
            for di, dj in directions:
                newI, newJ = i + di, j + dj
                if n > newI >= 0 and m > newJ >= 0 and grid[newI][newJ] == "1":
                    res += dfs(newI, newJ)
            
            return res

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1
        
        return ans