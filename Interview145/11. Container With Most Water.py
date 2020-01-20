"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""
def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s = 0
        left = 0
        right = len(height)-1
        while right > left: #(right -left) >= 1:
            if height[left] < height[right]:
                s = max(s,height[left]*(right-left))
                left += 1
            else:   
                s = max(s,height[right]*(right-left))
                right -= 1
        return s
