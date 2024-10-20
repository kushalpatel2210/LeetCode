from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = Counter(arr)

        return len(list(occurences.values())) == len(set(occurences.values()))