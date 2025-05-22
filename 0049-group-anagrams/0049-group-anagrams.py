from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for word in strs:
            signature = [0] * 26

            for c in word:
                signature[ord(c) - ord('a')] += 1
            
            hashMap[tuple(signature)].append(word)
        
        return list(hashMap.values())