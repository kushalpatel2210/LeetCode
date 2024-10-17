class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len, word2_len = len(word1), len(word2)
        combined = []

        for i in range(len(word1)):
            combined.append(word1[i])
            if i < word2_len:
                combined.append(word2[i])

        if word2_len > word1_len:
            combined.append(word2[word1_len:])
        
        return ''.join(combined)
        
