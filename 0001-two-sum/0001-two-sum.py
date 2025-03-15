class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in dictionary:
                return [dictionary[diff], i]
            else:
                dictionary[num] = i
        
        