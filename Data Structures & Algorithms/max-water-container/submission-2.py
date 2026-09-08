class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        largest = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            largest = max(area, largest)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return largest
        