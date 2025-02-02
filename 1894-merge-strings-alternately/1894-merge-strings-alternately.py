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