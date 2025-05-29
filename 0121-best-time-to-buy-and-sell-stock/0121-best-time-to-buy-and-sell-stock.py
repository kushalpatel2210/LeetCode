class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        maxProfit = 0

        for price in prices:
            if price > buy:
                maxProfit = max(maxProfit, price - buy)
            else:
                buy = price
        
        return maxProfit