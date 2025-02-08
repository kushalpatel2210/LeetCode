class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26        

'''
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1)
            counterS1 = Counter(s1)
            store = Counter()
            l = 0

            if len(s2) < len(s1):
                return False

            for r in range(len(s2)):
                store[s2[r]] += 1

                while r - l + 1 > windowSize:
                    store[s2[l]] -= 1
                    if store[s2[l]] == 0:
                        del store[s2[l]]
                    l += 1

                if counterS1 == store:
                    return True
            
            return False
'''

'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1)
        sortedS1 = sorted(s1)
        store = Counter
        l = 0

        if len(s2) < len(s1):
            return False

        for r in range(len(s2)):
            store.append(s2[r])

            while r - l + 1 > windowSize:
                store.remove(s2[l])
                l += 1

            subString = ''.join(store)
            if sortedS1 == sorted(subString):
                return True
        
        return False
'''

                
'''
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        for r in range(len(s2)):
            frq = Counter(s1)

            while r < len(s2) and len(frq) != 0 and s2[r] in frq:
                frq[s2[r]] -= 1
                if frq[s2[r]] == 0:
                    del frq[s2[r]]
                r += 1
            
            if len(frq) == 0:
                return True
        
        return False
'''
