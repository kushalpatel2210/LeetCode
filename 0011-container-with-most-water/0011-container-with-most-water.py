class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxWater = 0

        while l < r:
            maxWater = max(maxWater, min(height[l], height[r]) * (abs(r - l)))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater