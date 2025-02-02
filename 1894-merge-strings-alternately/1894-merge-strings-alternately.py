class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i = j = 0
        res = []

        while j < m or j <n:
            if i < m:
                res.append(word1[i])
            
            if j < n:
                res.append(word2[i])
            
            i += 1
            j += 1
        
        return "".join(res)

'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        start1 = start2 = 0
        mergedString = ''

        while start1 < len(word1) and start2 < len(word2):
            mergedString += word1[start1] + word2[start2]
            start1 += 1 
            start2 += 1 
        
        if start1 < len(word1):
            mergedString += word1[start1::]
        
        if start2 < len(word2):
            mergedString += word2[start2::]

        return mergedString
'''