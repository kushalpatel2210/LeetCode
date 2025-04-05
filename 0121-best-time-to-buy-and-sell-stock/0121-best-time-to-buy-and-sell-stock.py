class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximumProfit = 0
        buy = float('inf')

        for price in prices:
            if price <= buy:
                buy = price
            else:
                maximumProfit = max(maximumProfit, price - buy)
            
        return maximumProfit
