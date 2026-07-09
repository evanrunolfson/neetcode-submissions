class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #we don't want to sort this one.
        
        left = 0
        right = len(heights) - 1 #7
        max_area = 0

        while left < right:
            
            if heights[left] < heights[right]:
                height = heights[left]
            else:
                height = heights[right]

            area = height * (right-left)

            if area > max_area:
                max_area = area
            
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        
        return max_area

        