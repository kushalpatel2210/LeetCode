class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft, maxRight = [0] * n, [0] * n
        left, right = 0, 0
        trappedWater = 0

        for i in range(len(height)):
            if i - 1 >= 0:
                maxLeft[i] = left
            left = max(left, height[i])
        
        for i in range(len(height) - 1, -1, -1):
            if i + 1 < len(height):
                maxRight[i] = (right)
            right = max(right, height[i])

        # print(maxLeft)
        # print(maxRight)
        
        for i in range(len(height)):
            # print(f"i {i} maxlLeft[i] {maxLeft[i]} maxRight[i] {maxRight[i]}")
            containerSize = min(maxLeft[i], maxRight[i])
            # print(f"containerSize {containerSize}")
            trappedWater += (max(containerSize - height[i], 0))
            # print(trappedWater)

        return trappedWater
