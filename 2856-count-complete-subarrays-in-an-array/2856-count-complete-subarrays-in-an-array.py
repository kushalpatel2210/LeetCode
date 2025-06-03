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