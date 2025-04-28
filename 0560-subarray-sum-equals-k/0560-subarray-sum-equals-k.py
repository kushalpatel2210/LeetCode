from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = prefixSum = 0
        prefixSums = defaultdict(int)
        prefixSums[0] = 1

        for num in nums:
            prefixSum += num

            if prefixSum - k in prefixSums:
                count += prefixSums[prefixSum - k]
            
            prefixSums[prefixSum] += 1

        return count

'''
# Brute Force
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subArrays = 0

        for i in range(len(nums)):
            currSum = 0
            for j in range(i, len(nums)):
                currSum += nums[j]
                if currSum == k:
                    subArrays += 1
        
        return subArrays
'''