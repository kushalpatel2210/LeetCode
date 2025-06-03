from collections import Counter

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        uniqueCount = len(set(nums))
        frq = Counter()
        count, length = 0, len(nums)
        l = 0

        for r in range(len(nums)):
            frq[nums[r]] += 1

            while len(frq) == uniqueCount:
                count += length - r
                frq[nums[l]] -= 1

                if frq[nums[l]] == 0:
                    frq.pop(nums[l])

                l += 1
        
        return count

'''
# Brute force
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinctElements = set(nums)
        count = 0
        
        for i in range(len(nums)):
            currSet = set()
            for j in range(i, len(nums)):
                currSet.add(nums[j])

                if len(currSet) == len(distinctElements):
                    count += 1

        return count
'''