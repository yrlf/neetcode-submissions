class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        l, r = 0, 0
        window = {}
        res = 0
        maxf = 0
        while r < n:
            c = s[r]
            window[c] = window.get(c, 0) + 1
            r += 1
            maxf = max(maxf, window[c])
            while maxf + k < r - l:
                d = s[l]
                window[d] -= 1
                if window[d] == 0:
                    del(window[d])
                l += 1

            res = max(res, r - l)
        
        return res