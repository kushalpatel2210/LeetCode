class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        maxProfit = 0

        for price in prices:
            if price <= buy:
                buy = price
            else:
                profit = price - buy
                maxProfit = max(maxProfit, profit)
        
        return maxProfit