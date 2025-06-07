class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        mostWater = 0

        while l < r:
            currWater = min(height[l], height[r]) * (r - l)
            mostWater = max(mostWater, currWater)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return mostWater