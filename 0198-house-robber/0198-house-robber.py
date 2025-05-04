class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # Two choises 
            # 1. Either you skip the current house
            # 2. If you choose to rob current house then you need to rob prev->prev house
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        return dp[n - 1]