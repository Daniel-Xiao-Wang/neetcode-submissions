class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxHeight = 0
        
        while left < right:
            height = min(heights[left], heights[right]) * (right - left)
            if height > maxHeight:
                maxHeight = height
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxHeight