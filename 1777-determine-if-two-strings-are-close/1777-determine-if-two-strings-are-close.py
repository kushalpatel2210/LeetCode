from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False
        
        counter1, counter2 = Counter(word1), Counter(word2)
        occurences1_list, occurences2_list = list(counter1.values()), list(counter2.values())
        
        occurences1_list.sort()
        occurences2_list.sort()
        
        keys_match = set(counter1.keys()) == set(counter2.keys()) 

        return occurences1_list == occurences2_list and keys_match