class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = float('-inf')
        buy = float('inf')

        for price in prices:
            sell = price - buy

            if price < buy:
                buy = price
                continue
            
            profit = max(profit, sell)
        
        return profit if profit != float('-inf') else 0
