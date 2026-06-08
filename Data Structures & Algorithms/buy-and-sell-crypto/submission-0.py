class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')

        n = len(prices)
        ans = float('-inf')
        i = 0

        while i < n:
            ans = max(ans, prices[i] - lowest)
            lowest = min(lowest, prices[i])
            i += 1
        
        return max(0, ans)