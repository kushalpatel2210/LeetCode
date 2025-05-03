# Bottom-up DP
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
            
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

'''
# Top Down DP
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(step):
            if step <= 2:
                return step
            
            if step in memo:
                 return memo[step]
            
            memo[step] = dp(step - 1) + dp(step - 2)

            return memo[step]
'''