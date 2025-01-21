from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp_anagrams = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            grp_anagrams[key].append(word)
        
        return list(grp_anagrams.values())