class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        for i in range(1, len(prices)):
            if prices[i- 1] < prices[i]:
                maxProfit += prices[i] - prices[i - 1]
        
        return maxProfit

'''
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
'''
                