class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(i, j, idx):

            if idx == len(word)-1:
                return True            

            path.add((i, j))
            res = False
            for dx, dy in directions:
                newI, newJ = i + dx, j+dy
                if m > newI >= 0 and n > newJ >= 0 and (newI, newJ) not in path and word[idx+1] == board[newI][newJ]:
                    res = res or dfs(newI, newJ, idx+1)
            path.remove((i,j))
            return res
        

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    path = set()
                    if dfs(i, j, 0):
                        return True
        
        return False
