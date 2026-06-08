class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # O(N2), O(N2)

        # row: row_num -> set(1, 2, ...) for ith row, store its corresponding elements (global)
        # col: col_num -> set(1, 2, ...) 
        # block: set(1,2...) -> for each miniblock, we use this to store its corresponding elements

        # check miniblock with top left coord (i, j)

        row = defaultdict(set)
        col = defaultdict(set)

        def check_miniblock(i, j):
            block = set()
            for x in range(i, i+3):
                for y in range(j, j+3):                    
                    curr = board[x][y]
                    if curr == '.':
                        continue
                    
                    if curr in block or curr in row[x] or curr in col[y]:
                        return False
                    block.add(curr)
                    row[x].add(curr)
                    col[y].add(curr)
            
            return True

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                res = check_miniblock(i, j)
                if res == False:
                    return False
        

        return True