class Solution:
    def arrangeCoins(self, n: int) -> int:
        start, end = 0, n
        res = 0

        while start <= end:
            mid = start + (end - start) // 2
            currentSum = mid * (mid + 1) // 2
            
            if currentSum <= n:
                res = max(res, mid)
                start = mid + 1
            else:
                end = mid - 1
        
        return res