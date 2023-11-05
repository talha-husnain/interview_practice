class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        max_area = 0
        while left < right:
            w = right - left
            h = min(height[right], height[left])
            max_area = max(max_area, h*w)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
