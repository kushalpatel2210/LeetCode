from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_element = max(counter, key=counter.get)

        return max_element