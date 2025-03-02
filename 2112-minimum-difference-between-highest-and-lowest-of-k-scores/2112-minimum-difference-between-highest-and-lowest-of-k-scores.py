class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l , r = 0 , k - 1
        minScore = float('inf')
        
        while r < len(nums):
            minScore = min(minScore, nums[r] - nums[l])
            l += 1
            r += 1

        return minScore