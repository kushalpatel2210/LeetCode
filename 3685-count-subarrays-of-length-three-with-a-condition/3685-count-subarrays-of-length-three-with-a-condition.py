class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        currSum = 0
        i = 0
        res = 0

        for j in range(len(nums)):
            currSum += nums[j]

            if j - i + 1 < 3:
                continue

            middleNum = nums[j - 1]
            currSum -= middleNum

            if currSum == (middleNum / 2):
                res += 1
            
            currSum -= nums[i]
            currSum += middleNum
            i += 1
        
        return res

