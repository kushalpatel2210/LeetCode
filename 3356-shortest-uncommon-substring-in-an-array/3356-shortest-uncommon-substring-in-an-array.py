from collections import defaultdict

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        s = arr[0]
        subStringsMap = defaultdict(set)
        shortest = []

        for idx, word in enumerate(arr):
            for i in range(len(word)):
                for j in range(i + 1, len(word) + 1):
                    subStringsMap[idx].add(word[i:j])
        
        for key in subStringsMap:
            values = sorted(list(subStringsMap[key]), key=lambda x: (len(x), x))    
            combinedSet = set().union(*(subStringsMap[i] for i in range(len(subStringsMap)) if i != key))
            
            res = ''
            for subString in values:
                if subString not in combinedSet:
                    res = subString
                    break

            shortest.append(res)

        return shortest