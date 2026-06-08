class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [float('-inf')] + heights + [float('-inf')]
        n = len(heights)
        stk = []
        res = 0
        i = 0
        while i < n:
            #print(heights[i])
            while stk and  heights[i] < heights[stk[-1]]:
                idx = stk.pop()
            
                prev = stk[-1]
               
                width = (i - prev) - 1
                area = heights[idx] * width
                res = max(res, area)
                #print(f"pop {idx}, val {heights[idx]}, width {width}, area = {area}")
            stk.append(i)
            i += 1

        return res