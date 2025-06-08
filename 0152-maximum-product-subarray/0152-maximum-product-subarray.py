class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        currMax = currMin = 1

        for n in nums:
            tmp = n * currMax
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(tmp, n * currMin, n)
            res = max(res, currMax)
        
        return res