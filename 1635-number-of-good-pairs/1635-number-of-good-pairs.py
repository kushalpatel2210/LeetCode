from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = 0 

        for num in nums:
            res += count[num]
            count[num] += 1
        
        return res