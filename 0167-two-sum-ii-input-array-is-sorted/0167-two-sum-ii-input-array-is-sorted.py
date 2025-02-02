class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(numbers):
            diff = target - num

            if diff in hashMap:
                return [hashMap[diff] + 1, i + 1]
            
            hashMap[num] = i
        