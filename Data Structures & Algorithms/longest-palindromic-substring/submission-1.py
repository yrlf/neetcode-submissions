class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0 for _ in range (n)] for _ in range(n)]


        def check(i, j):

            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            
            return s[i+1:j], j - i - 1

        maxLength = 0
        output = ""
        for i in range(n):
            res1, length1 = check(i, i)
            if length1 > maxLength:
                maxLength = length1
                output = res1
            if i < n:
                res2, length2 =check(i, i+1)
                if length2 > maxLength:
                    maxLength = length2
                    output = res2

        return output