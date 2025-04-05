# DP - Top-up: Memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = { 0 : 1 }

        def steps(currStep):
            if currStep < 0:
                return 0
            elif currStep in memo:
                return memo[currStep]
            else:
                memo[currStep] = steps(currStep - 1) + steps(currStep - 2)
                return memo[currStep]

        return steps(n)

'''
# DP - Top-up: Memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = { 0 : 1 }

        def steps(currStep):
            if currStep < 0:
                return 0
            elif currStep in memo:
                return memo[currStep]
            else:
                memo[currStep] = steps(currStep - 1) + steps(currStep - 2)
                return memo[currStep]

        return steps(n)

# DP - Bottom-up: Tabulation
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

# DP - Bottom-up: memory optimized
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev, curr = 1, 2

        for i in range(n - 2):
            prev, curr = curr, prev + curr
        
        return curr
'''