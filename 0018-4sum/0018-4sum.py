class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                currSum = nums[i] + nums [j]
                if j + 1 < len(nums):
                    pair = self.pairSum(j + 1, len(nums) - 1, target - currSum, nums)
                    if pair:
                        res.add(tuple([nums[i], nums[j]] + pair))
        
        return [list(quadraple) for quadraple in res]

    def pairSum(self, left, right, target, nums):
        while left < right:
            currSum = nums[left] + nums[right]

            if currSum == target:
                return [nums[left], nums[right]]
            elif currSum < target:
                left += 1
            else:
                right -= 1
        
        return []