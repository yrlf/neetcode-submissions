class TreeNode:
    
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        p = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if p.children[idx] == None:
                p.children[idx] = TreeNode()
            p = p.children[idx]
        p.isEnd = True

    def search(self, word: str) -> bool:
        p = self.root

        for w in word:
            idx = ord(w) - ord('a')
            if p.children[idx] == None:
                return False
            p = p.children[idx]
        
        return True if p.isEnd else False

    def startsWith(self, prefix: str) -> bool:
        p = self.root

        for w in prefix:
            idx = ord(w) - ord('a')
            if p.children[idx] == None:
                return False
            p = p.children[idx]
        return True
        
        