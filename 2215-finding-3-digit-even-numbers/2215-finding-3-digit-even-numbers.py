from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        res = []

        for num in range(100, 1000, 2):
            parts = [int(d) for d in str(num)]
            count = Counter(parts)
            if all(freq[d] >= count[d] for d in count):
                res.append(num)
        
        return res
