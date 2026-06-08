class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [[ False for _ in range(n)] for _ in range(n)]

        
        cnt = 0

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                else:
                    if i + 1 < n and j - 1 >= 0 and s[i] == s[j] and (j - i <= 1 or dp[i+1][j-1] == True):
                        dp[i][j] = True
                
        for i in range(n):
            for j in range(n):
                if dp[i][j] == True:
                    cnt += 1

        return cnt
                        