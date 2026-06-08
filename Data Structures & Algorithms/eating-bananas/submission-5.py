class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles) + 1

        def check(x):
            days = 0
            for i in range(len(piles)):
                if piles[i] % x != 0:
                    days += piles[i]//x + 1
                else:
                    days += piles[i] // x
            
            return days <= h

        while l < r:
            mid = (l+r)//2
            if check(mid):
                r = mid
            else:
                l = mid+1
        
        return l