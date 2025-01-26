from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        kFrequent = counter.most_common(k)
        result = []

        for ele in kFrequent:
            result.append(ele[0])

        return result