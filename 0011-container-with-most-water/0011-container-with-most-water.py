class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxWater = 0

        while l < r:
            currWater = (r - l) * min(height[l], height[r])
            maxWater = max(maxWater, currWater)

            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else: # Both are equal
                l += 1
                r -= 1
        
        return maxWater
