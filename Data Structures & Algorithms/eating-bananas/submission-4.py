class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        def check(rate):
            # return True if it's doable within h hours
            time = 0
            for i in range(n):
                if piles[i] % rate != 0:
                    time += piles[i]//rate + 1
                else:
                    time += piles[i] // rate 
            return time <= h
        
        # [l, r)
        l, r = 1, max(piles) + 1 # [l, r) -> [1, 4] = [1, 5)
        
        # [l, r]
        l, r = 1, max(piles)

        # (l, r)  ->       ....l] [l+1, r-1] [r,.......      

        l, r = 0, max(piles) + 1
        while l +1 < r:
            mid = (l+r) >> 1
            if check(mid):
                r = mid
            else:
                l = mid
        

        return r
