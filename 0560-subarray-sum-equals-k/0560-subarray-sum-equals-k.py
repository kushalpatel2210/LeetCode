from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        hashMap = defaultdict(int) # prefix: count
        hashMap[0] = 1
        count = 0

        for num in nums:
            prefixSum += num

            if prefixSum - k in hashMap:
                count += hashMap[prefixSum - k]
            
            hashMap[prefixSum] += 1
        
        return count