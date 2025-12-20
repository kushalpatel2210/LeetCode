from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list) # key: tuple, val: list

        for word in strs:
            key = [0] * 26

            for c in word:
                key[ord(c) - ord('a')] += 1

            hashMap[tuple(key)].append(word)
        
        return list(hashMap.values())