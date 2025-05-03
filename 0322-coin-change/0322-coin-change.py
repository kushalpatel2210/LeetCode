# Bottom-up DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] if dp[amount] != float('inf') else -1


'''
# Top Down DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(target):
            if target == 0:
                return 0
            
            if target in memo:
                return memo[target]
            
            minCoins = float('inf')
            for coin in coins:
                if coin <= target:
                    minCoins = min(minCoins, 1 + dp(target - coin))
            memo[target] = minCoins

            return memo[target]

        return dp(amount) if dp(amount) != float('inf') else -1
'''