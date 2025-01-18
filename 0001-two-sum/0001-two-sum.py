class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i, num in enumerate(nums):
            diff = target - num
            if num in dict:
                return [i, dict[num]]
            dict[diff] = i

        return None