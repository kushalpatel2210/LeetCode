from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for word in strs:
            frq = [0] * 26

            for c in word:
                frq[ord(c) - ord('a')] += 1
            
            hashMap[tuple(frq)].append(word)
        
        return [list(values) for values in hashMap.values()]