class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        maxVowels, currVowels = 0, 0

        for i in range(k):
            if s[i] in vowels:
                currVowels += 1
        
        maxVowels = currVowels
        
        for i in range(k, len(s)):
            if s[i] in vowels:
                currVowels += 1
            if s[i - k] in vowels:
                currVowels -= 1
            maxVowels = max(maxVowels, currVowels)
        
        return maxVowels

                