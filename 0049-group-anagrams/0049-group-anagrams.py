from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for word in strs:
            sortedWord = ''.join(sorted(word))
            hashMap[sortedWord].append(word)
        
        return list(hashMap.values())
