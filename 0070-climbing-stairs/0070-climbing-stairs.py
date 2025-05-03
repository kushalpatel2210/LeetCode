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
        
        return dp(n)