class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0 
        minLength = float('inf')
        currentSum = 0

        for j in range(len(nums)):
            currentSum += nums[j]

            # condition
            while currentSum >= target:
                minLength = min(minLength, j - i + 1)

                # Shrink window 
                currentSum -= nums[i]
                i += 1
        
        return minLength if minLength != float('inf') else 0