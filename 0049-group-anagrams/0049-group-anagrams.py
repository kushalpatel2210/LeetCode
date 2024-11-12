from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)

        for str in strs:
            sorted_str = ''.join(sorted(str))
            dictionary[sorted_str].append(str)
        
        return list(dictionary.values())
        