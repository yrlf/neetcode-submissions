class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        m, n = len(grid), len(grid[0])

        directions = [[1,0],[0,1],[-1,0],[0,-1]]


        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        visited = set()
        step = 0
        while q:
            size = len(q)

            for _ in range(size):
                row, col = q.popleft()

                for dx, dy in directions:
                    nrow, ncol = row + dx, col + dy
                    if m > nrow >= 0 and n > ncol >= 0 and grid[nrow][ncol] == INF:
                        grid[nrow][ncol] = step + 1
                        q.append((nrow, ncol))
            step += 1
        

    


