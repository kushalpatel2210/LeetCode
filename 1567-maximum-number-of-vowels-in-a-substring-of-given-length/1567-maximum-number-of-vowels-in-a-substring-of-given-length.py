class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxCount = float('-inf')
        l = 0
        currCount = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for r in range(len(s)):
            if s[r] in vowels:
                currCount += 1

            if r - l + 1 < k:
                continue
            
            maxCount = max(maxCount, currCount)
            if s[l] in vowels:
                currCount -= 1
            l += 1
        
        return maxCount
