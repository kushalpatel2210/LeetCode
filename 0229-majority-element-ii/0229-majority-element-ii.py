from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frq = Counter(nums)
        total = len(nums)
        result = []

        for ele, frequency in frq.items():
            if frequency > ( total / 3 ):
                result.append(ele)

        return result       