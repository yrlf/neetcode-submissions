class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        l, r = 0, 0
        cnt = Counter(t)
        cnt_s = Counter(s)

        for char, freq in cnt.items():
            if char not in s or freq > cnt_s[char]:
                return ""


        window = {}
        valid = 0
        
        res = s

        while r < n:
            c = s[r]
            window[c] = window.get(c, 0) + 1
            r += 1

            if c in cnt and window[c] == cnt[c]:
                valid += 1
            
            
            while valid == len(cnt) and l <= r:
                if r - l < len(res):
                    res = s[l:r]
                print(valid, res)
                d = s[l]
                if window[d] == cnt[d]:
                    valid -= 1
                window[d] -= 1
                l += 1
                        

        return res
