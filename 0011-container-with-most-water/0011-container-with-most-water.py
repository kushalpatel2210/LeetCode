class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0, len(height) - 1
        maxWater = 0

        while left < right:
            water = (right - left) * min(height[left], height[right])
            maxWater = max(maxWater, water)

            if left < right:
                left += 1
            else:
                right -= 1
        
        return maxWater