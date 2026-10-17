class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        l, r = 0, len(heights) - 1
        while l < r:
            water = (r-l) * min(heights[l], heights[r])
            largest = max(water, largest)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return largest
        