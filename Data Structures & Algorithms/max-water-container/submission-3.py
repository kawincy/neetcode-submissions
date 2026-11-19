class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #for any given window, the area will never increase if the taller side is moved in
        l = 0
        r = len(heights) - 1
        result = 0
        while l < r:
            shorter = min(heights[l], heights[r])
            result = max(result, shorter * (r-l) )
            if heights[l] == shorter: l += 1
            else: r -= 1
        return result