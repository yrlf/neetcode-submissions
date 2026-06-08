class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        # 1. check from left and right ends and moving the 2 pointers towards central 
        # O(N), O(1) 

        def isInvalid(c):
            if (not c.isalnum()):
                return True

        n = len(s)
        if (n < 2): return True

        l, r = 0, n-1

        while l <= r:
            while l < n and isInvalid(s[l]):
                l += 1
            while r >= 0 and isInvalid(s[r]):
                r -= 1

            if l < n and r >= 0 and s[l].lower() != s[r].lower():  # 
                return False
            else:
                l += 1
                r -= 1
        
        return True
            

