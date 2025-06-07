from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for s in strs:
            key = [0] * 26

            for c in s:
                key[ord(c) - ord('a')] += 1
            
            hashMap[tuple(key)].append(s)
        
        return [list(x) for x in hashMap.values()]