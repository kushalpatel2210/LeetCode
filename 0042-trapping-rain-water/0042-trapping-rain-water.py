class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft, maxRight = [0] * n, [0] * n
        left, right = 0, 0
        trappedWater = 0

        maxLeft[0] = height[0]
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i])
        
        maxRight[n - 1] = height[n - 1]
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i])   
        
        for i in range(len(height)):
            containerSize = min(maxLeft[i], maxRight[i])
            trappedWater += containerSize - height[i]

        return trappedWater
