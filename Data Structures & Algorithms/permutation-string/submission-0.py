class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m1 = Counter(s1)
        window = {}

        n = len(s1)
        m = len(s2)
        l, r = 0, 0
        valid = 0

        while r < m:
            c = s2[r]
            r += 1
            if c not in window:
                window[c] = 0
            window[c] += 1
            if c in m1 and window[c] == m1[c]:
                valid += 1

            while l < r and r - l > n:
                d = s2[l]
                if d in m1 and window[d] == m1[d]:
                    valid -= 1
                
                window[d] -= 1
                if window[d] == 0:
                    del(window[d])
                l+=1
        

            if  r - l == n and valid == len(m1):
                return True
        
        return False