from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        res = 0

        for num in nums:
            currSum += num
            diff = currSum - k
            res += prefixSum[diff]
            prefixSum[currSum] += 1
        
        return res
