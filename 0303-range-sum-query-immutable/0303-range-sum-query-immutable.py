class NumArray:

    def __init__(self, nums: List[int]):
        self.totalSum = sum(nums)

        n = len(nums)
        self.prefix = [0] * n
        self.suffix = [0] * n
        
        prefixSum = 0
        suffixSum = 0
        
        for i, num in enumerate(nums):
            self.prefix[i] = prefixSum 
            prefixSum += num
        
        for i in range(n - 1, -1, -1):
            self.suffix[i] = suffixSum
            suffixSum += nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.totalSum - self.prefix[left] - self.suffix[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)