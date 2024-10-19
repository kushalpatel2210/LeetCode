class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg, currSum = 0, 0

        for i in range(k):
            currSum += nums[i]
        
        avg = currSum / k

        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i - k]
            currAvg = currSum / k
            avg = max(avg, currAvg)

        return avg