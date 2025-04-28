class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = startIndex = currSum = 0

        for endIndex, val in enumerate(nums):
            currSum += val 

            while currSum * (endIndex - startIndex + 1) >= k:
                currSum -= nums[startIndex]
                startIndex += 1
            
            ans += (endIndex - startIndex + 1)
        
        return ans