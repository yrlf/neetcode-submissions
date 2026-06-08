class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0]*26
        m, n = len(s), len(t)
        if m != n:
            return False
        for i in range(m):
            record[ord(s[i]) - ord('a')] += 1
            record[ord(t[i]) - ord('a')] -= 1
        
        for i in range(26):
            if (record[i] != 0):
                return False
        
        return True

        
