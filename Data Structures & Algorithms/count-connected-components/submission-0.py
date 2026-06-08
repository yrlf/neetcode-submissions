
class UF:
    def __init__(self, n):
        self.n = n
        self.parents = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def union(self, p, q):
        rootP, rootQ = self.find(p), self.find(q)
        if rootP == rootQ:
            return
        
        if self.size[rootP] > self.size[rootQ]:
            self.parents[rootQ] = rootP
            self.size[rootP] = self.size[rootQ]
        else:
            self.parents[rootP] = rootQ
            self.size[rootQ] = self.size[rootP]
        
        self.n -= 1
    
    def find(self, p):
        if self.parents[p] != p:
            self.parents[p] = self.find(self.parents[p])
        
        return self.parents[p]

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for a, b in edges:
            uf.union(a,b)
        
        return uf.n