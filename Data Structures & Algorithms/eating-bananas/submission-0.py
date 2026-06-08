class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        def check(rate):
            time = 0
            for i in range(n):
                if piles[i] % rate != 0:
                    time += piles[i]//rate + 1
                else:
                    time += piles[i] // rate 
            return time <= h
        

        l, r = 1, max(piles)

        while l < r:
            mid = (l+r) >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1
        
        return l