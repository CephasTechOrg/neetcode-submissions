class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights)-1
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            area = height * width
            max_area = max(max_area, area)

            if heights[left] < heights[right]:
                left =  left + 1
            elif heights[right] < heights[left]:
                right = right - 1 
            else:
                left += 1
                right -= 1 
        return max_area           
              
        
        