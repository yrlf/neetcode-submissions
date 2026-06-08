class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        l, r = 0, 0
        window = {}
        major = s[0]
        ans = 0

        while r < n:
            c = s[r]
            r += 1
            if c not in window:
                window[c] = 0
            window[c] += 1

            if window[c] > window[major]:
                major = c

            while (l < r and r - l - window[major] > k):
                d = s[l]
                window[d] -= 1

                if d == major:
                    for key, val in window.items():
                        if val > window[d]:
                            major = key
                
                if window[d] == 0:
                    del(window[d])
                
                l += 1
            
            ans = max(ans, r - l)
        
        return ans
                
