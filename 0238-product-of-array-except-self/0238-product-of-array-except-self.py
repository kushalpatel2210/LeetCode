class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftProd, rightProd = [0] * n, [0] * n
        leftProd[0], rightProd[n - 1] = 1, 1
        res = [0] * n

        for i in range(1, n):
            leftProd[i] = leftProd[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            rightProd[i] = rightProd[i + 1] * nums[i + 1]
        
        for i in range(n):
            res[i] = leftProd[i] * rightProd[i]

        return res
