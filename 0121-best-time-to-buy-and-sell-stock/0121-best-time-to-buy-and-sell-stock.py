class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maximumProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                maximumProfit = max(maximumProfit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        
        return maximumProfit

'''
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
'''