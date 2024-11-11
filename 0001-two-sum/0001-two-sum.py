class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = dict()

        for index, num in enumerate(nums):
            diff = target - num
            if num in store:
                return [index, store[num]]
            store[diff] = index
