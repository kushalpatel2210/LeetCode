class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        maxProfit = 0

        for price in prices:
            profit = max(0, price - buy)

            if profit > 0:
                maxProfit += profit
                buy = float('inf')
            
            if price <= buy:
                buy = price
        
        return maxProfit
                