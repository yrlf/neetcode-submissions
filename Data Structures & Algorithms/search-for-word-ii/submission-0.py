class TrieNode:
    def __init__(self, char):
        self.children = [None] * 26
        self.isEnd = False
        self.s = char

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def dfs(i, j, pointer):

            if pointer.isEnd == True:
                res.add(pointer.s)
            
            next_steps = set()

            for a in range(26):
                if pointer.children[a] != None:
                    next_steps.add(chr(ord('a') + a))
            
            used.add((i,j))
            for di, dj in directions:
                newI, newJ = i + di, j + dj
                if m > newI >= 0 and n > newJ >= 0:
                    if board[newI][newJ] in next_steps and (newI, newJ) not in used:
                    
                        newPointer = pointer.children[ord(board[newI][newJ])-ord('a')]
                        dfs(newI, newJ, newPointer)

            used.remove((i,j))

        root = TrieNode("")
        for word in words:
            p = root
            for w in word:
                if p.children[ord(w)-ord('a')] == None:
                    p.children[ord(w) - ord('a')] = TrieNode(p.s + w)
                p = p.children[ord(w) - ord('a')]
            p.isEnd = True
        
        m, n = len(board), len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        res = set()

        used = set()

        for i in range(m):
            for j in range(n):
                p = root
                if p.children[ord(board[i][j]) - ord('a')] != None:
                    p = p.children[ord(board[i][j]) - ord('a')]
                    dfs(i, j, p)


        return list(res)