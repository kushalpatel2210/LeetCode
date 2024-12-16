class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0 
        j = len(height) - 1
        maxWater = float('-inf')

        while i < j:
            # Process
            currentWater = (j - i) * min(height[i], height[j])
            maxWater = max(maxWater, currentWater)

            # Increment or decrement counter
            if height[i] < height[j]:
                i += 1 
            else:
                j -= 1
        
        return maxWater