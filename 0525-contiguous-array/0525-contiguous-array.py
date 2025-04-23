class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zeroCount, oneCount = 0, 0
        maxLength = 0
        diffIndex = dict() # diff, index

        for i, num in enumerate(nums):
            if num == 0:
                zeroCount += 1
            else:
                oneCount += 1

            diff = oneCount - zeroCount
            if diff not in diffIndex:
                diffIndex[diff] = i
            
            if zeroCount == oneCount:
                maxLength = zeroCount + oneCount
            else:
                idx = diffIndex[diff]
                maxLength = max(maxLength, i - idx)
        
        return maxLength
            
