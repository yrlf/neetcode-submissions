class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        n = len(s)
        l, r = 0, 0
        
        ans = 0

        while r < n:
            c = s[r]
            r += 1
            
            if c not in window:
                window[c] = 1
            else:
                window[c] += 1

            while l < r and window[c] > 1:
                d = s[l]
                window[d] -= 1
                if window[d] == 0:
                    del(window[d])
                l+=1
            
            ans = max(ans, r - l)
        
        return ans