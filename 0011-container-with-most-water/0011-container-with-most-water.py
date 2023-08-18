class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while (left < right) :
            # calculate area between the current left and right index
            area = min(height[left], height[right]) * (right - left)
            # storing max area each time
            max_area = max(area, max_area)
            
            # move the index towards each other based on their values
            if (height[left] >= height[right]) :
                right = right - 1              # move the right index towards left 
            else :
                left = left + 1                # move the left index towards right
        
        return max_area