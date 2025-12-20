class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff in store:
                return [store[diff], i]
            store[num] = i 