class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()
        
        def dfs(target):
            if target == 0:
                return 0

            if target in memo:
                return memo[target]

            res = float('inf')
            for coin in coins:
                if target - coin >= 0:
                    res = min(res, 1 + dfs(target - coin))
            memo[target] = res

            return res

        minCoins = dfs(amount)
        return minCoins if minCoins != float('inf') else -1
