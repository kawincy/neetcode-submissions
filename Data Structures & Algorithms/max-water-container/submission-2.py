class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = self.calculateArea(left, right, heights)
        while left < right:
            if heights[left] < heights[right]:
                left += 1
                area = max(area, self.calculateArea(left, right, heights))
            else:
                right -= 1
                area = max(area, self.calculateArea(left, right, heights))
        return area

    def calculateArea(self, l, r, heights):
        return min(heights[l],heights[r]) * (r - l)
        