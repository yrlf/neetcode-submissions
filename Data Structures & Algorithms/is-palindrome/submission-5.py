class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # clean string

        n = len(s)
        newS = ""
        for i in range(n):
            if s[i].isalnum():
                newS += s[i].lower()
        

        # tab a cat
        
        # print(newS)
        m = len(newS)
        p, q = 0, m-1
        while p < m and q >= 0 and p <= q:
            # print(newS[p], newS[q])
            if newS[p] != newS[q]:
                return False
            p += 1
            q -= 1
        
        return True