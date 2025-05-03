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
