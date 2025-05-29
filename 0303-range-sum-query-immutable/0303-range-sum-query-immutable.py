class NumArray:

    def __init__(self, nums: List[int]):    
        n = len(nums)
        prefixSum = 0
        self.prefix = [0] * n
        self.totalSum = sum(nums)
        
        for i, num in enumerate(nums):
            prefixSum += num
            self.prefix[i] = prefixSum 

    def sumRange(self, left: int, right: int) -> int:
        leftSum = self.prefix[left - 1] if left > 0 else 0
        rightSum = self.prefix[right]
        return rightSum - leftSum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)