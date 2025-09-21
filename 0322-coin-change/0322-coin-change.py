class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()

        def dp(target):
            if target == 0:
                return 0
            
            if target in memo:
                return memo[target]
            
            res = float('inf')
            for coin in coins:
                if target - coin >= 0:
                    res = min(res, 1 + dp(target - coin))
            memo[target] = res
            return res

        minCoins = dp(amount)
        return minCoins if minCoins != float('inf') else -1