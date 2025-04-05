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