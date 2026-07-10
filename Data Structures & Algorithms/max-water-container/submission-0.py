class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lmax, rmax = heights[0], heights[-1]
        n = len(heights)
        l, r = 0, n-1

        res = 0

        while l < r:
            h = min(heights[l], heights[r])
            w = r - l
            res = max(res, h * w)

            if heights[l] > heights[r]:
                
                r -= 1
            else:
                l += 1

        return res